import cv2
import re
import torch
from transformers import AutoProcessor, AutoModelForVision2Seq
from huggingface_hub import hf_hub_download

# ────────────────────────────────────────────────────────────────────────────────
# CONFIGURATION
MODEL_ID            = "ibm-granite/granite-vision-3.2-2b"  # Granite Vision 3.2 2B :contentReference[oaicite:3]{index=3}
THRESHOLD           = 20                                 # Maximum people allowed
VIDEO_SOURCE        = 0                                  # 0=webcam or replace with RTSP URL
NOTIFICATION_DELAY  = 2 * 60 * 60                        # 2 hours in seconds
# ────────────────────────────────────────────────────────────────────────────────

# Device setup
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load processor & model
processor = AutoProcessor.from_pretrained(MODEL_ID)                          # vision+text processor :contentReference[oaicite:4]{index=4}
model     = AutoModelForVision2Seq.from_pretrained(MODEL_ID).to(device)      # multimodal model :contentReference[oaicite:5]{index=5}
model.eval()

# Fetch a test image to warm up (optional)
_ = hf_hub_download(repo_id=MODEL_ID, filename="example.png")

last_notification_time = 0

def notify_overcrowd(count: int):
    """Placeholder: integrate IBM WatsonX/Granite notification here."""
    print(f"[ALERT] Detected {count} people—clinic at capacity!")
    print("🚫 Block new registrations. Ask next visitor to return in 2 hours.\n")
    # TODO: call IBM Cloud Functions / WatsonX API to send SMS/email or update booking system

def extract_count(answer: str) -> int:
    """Extract the first integer found in the model’s free-text answer."""
    match = re.search(r"\b(\d+)\b", answer)
    return int(match.group(1)) if match else 0

def count_people(frame) -> int:
    """Run Granite Vision to ask: 'How many people are present in this image?'"""
    # Convert BGR→RGB and to PIL-like input
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Build multimodal chat prompt
    conversation = [
        {"role":"user", "content":[
            {"type":"image", "url": image},
            {"type":"text",  "text": "How many people are present in this image?"}
        ]}
    ]
    inputs = processor.apply_chat_template(
        conversation,
        add_generation_prompt=True,
        tokenize=True,
        return_tensors="pt"
    ).to(device)
    # Generate answer
    outputs = model.generate(**inputs, max_new_tokens=16)
    answer  = processor.decode(outputs[0], skip_special_tokens=True)
    return extract_count(answer)

def main():
    global last_notification_time

    cap = cv2.VideoCapture(VIDEO_SOURCE)
    if not cap.isOpened():
        raise RuntimeError(f"Cannot open video source {VIDEO_SOURCE}")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        count = count_people(frame)
        # Overlay count
        cv2.putText(frame, f"People: {count}", (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)

        # Overcrowd logic
        now = torch.tensor(torch.time.time()).item()
        if count >= THRESHOLD and now - last_notification_time > NOTIFICATION_DELAY:
            notify_overcrowd(count)
            last_notification_time = now

        cv2.imshow("Granite Vision Crowd Counter", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
