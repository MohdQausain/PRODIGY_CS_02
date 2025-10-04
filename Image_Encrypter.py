from PIL import Image
import numpy as np
from tkinter import Tk, filedialog

# Setup Tkinter
root = Tk()
root.withdraw()
root.attributes('-topmost', True)  # Make dialogs appear in front

def scramble_image(image_path, key, save_path, mode="encrypt"):
    img = Image.open(image_path)
    arr = np.array(img)
    shape = arr.shape
    flat_arr = arr.reshape(-1, arr.shape[2])

    rng = np.random.default_rng(key)
    indices = np.arange(len(flat_arr))
    
    if mode == "encrypt":
        rng.shuffle(indices)
        scrambled = flat_arr[indices]
    else:  # decrypt
        rng.shuffle(indices)
        unscrambled = np.empty_like(flat_arr)
        unscrambled[indices] = flat_arr
        scrambled = unscrambled

    result_img = scrambled.reshape(shape)
    Image.fromarray(result_img).save(save_path)
    print(f"Image {mode}ed successfully. Saved at: {save_path}")

def main():
    choice = input("Encrypt (e) or Decrypt (d)? ").lower()
    if choice not in ["e", "d"]:
        print("Invalid choice.")
        return

    key = int(input("Enter numeric key: "))

    print("Select image file...")
    img_path = filedialog.askopenfilename(filetypes=[("Image files","*.png;*.jpg;*.jpeg;*.bmp")])
    if not img_path:
        print("No file selected. Exiting.")
        return

    save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG","*.png"),("JPEG","*.jpg"),("BMP","*.bmp")])
    if not save_path:
        print("No save location selected. Exiting.")
        return

    mode = "encrypt" if choice == "e" else "decrypt"
    scramble_image(img_path, key, save_path, mode)

    # Pause so CMD doesn’t close immediately
    input("Operation finished. Press Enter to exit...")

if __name__ == "__main__":
    main()
