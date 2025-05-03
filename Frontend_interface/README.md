# Yolov8_count_class

 Ultralytics YOLOv8 Region Counter for a specific class



This repository contains an implementation of an enhanced object tracking system using Ultralytics YOLOv8. The project is focused on counting objects within defined regions in video feeds. It allows for real-time updating of regions and supports tracking multiple regions simultaneously.
Features

    Integration with Ultralytics YOLOv8 for object detection.
    Customizable region-based counting.
    Real-time updating of regions via a graphical user interface.
    Support for multiple counting regions with individual tracking.
    Adjustable parameters for detection and tracking.

# Installation

To use this project, follow these steps:

    Clone the repository:

git clone https://github.com/msedki/Yolov8_count_class.git

Install required dependencies (assuming you have Python and pip installed):

    pip install -r requirements.txt

# Usage

 To run the region counter for a specific class exemple Number 2 :

    Set up your environment with the necessary dependencies.
    Execute the script with the desired parameters. For example:

    python yolov8class.py --weights yolov8n.pt --view-img --class-id 2

# Command Line Arguments

    --weights: Path to the model weights file (default: 'yolov8n.pt').
    --view-img: Flag to display the output window.
    --save-img: Flag to save the output images.
    --line-thickness: Bounding box thickness.
    --region-thickness: Region box thickness.
    --class-id: ID of the class to count.

# Contributing

Contributions to improve the project are welcome. Please follow these steps:

    Fork the repository.
    Create a new branch for your feature (git checkout -b feature/AmazingFeature).
    Commit your changes (git commit -m 'Add some AmazingFeature').
    Push to the branch (git push origin feature/AmazingFeature).
    Open a pull request.

# Acknowledgements

    Ultralytics for YOLOv8.
    Contributors and maintainers of this project.
