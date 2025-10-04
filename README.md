# PRODIGY_CS_02
Prodigy Cyber Security Internship - Task 2 - Pixel Manipulation for Image Encryption
Here’s the updated GitHub description with both **Pillow** and **NumPy** installation instructions clearly mentioned:

---

# 🔒 Image Scrambler

A fun Python tool to **encrypt** and **decrypt images** by scrambling their pixels with a numeric key.
Perfect for experimenting with image manipulation, numpy shuffling, and basic cryptography concepts.

## ✨ Features

* Encrypt any image (`.png`, `.jpg`, `.jpeg`, `.bmp`) into a scrambled version.
* Decrypt back to the original using the same numeric key.
* Deterministic shuffling with **NumPy’s** random generator.
* Simple GUI file picker using **Tkinter** (no need to type file paths).
* Supports multiple save formats (`.png`, `.jpg`, `.bmp`).

## 🚀 Usage

1. Run the script:

   ```bash
   python image_scrambler.py
   ```
2. Choose whether to **Encrypt (e)** or **Decrypt (d)**.
3. Enter a numeric key (use the same key for decryption).
4. Select an image file.
5. Choose a location to save the output.

## ⚙️ Installation

* Make sure you have **Pillow** and **NumPy** installed:

  ```bash
  pip install pillow numpy
  ```

> If you see an error like `ModuleNotFoundError: No module named 'PIL'` or `ModuleNotFoundError: No module named 'numpy'`, installing these packages will fix it.

## 🛠️ Tech Stack

* **Python**
* **Pillow (PIL)** – image handling
* **NumPy** – pixel shuffling
* **Tkinter** – file dialogs

## 🎯 Why build this?

A playful way to explore **randomization**, **deterministic shuffling**, and **image processing**, all wrapped in a simple GUI.
