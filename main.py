import os
import subprocess
import sys
import cv2
import pyautogui

def main():
    # Take a screenshot
    current_directory = os.getcwd()
    output_file = os.path.join(current_directory, 'capture.png')
    subprocess.check_output(['screencapture', '-x', output_file], shell=False)

    # Detect the box within the screenshot
    method = cv2.TM_SQDIFF_NORMED
    small_image = cv2.imread('box.png')
    large_image = cv2.imread('capture.png')
    result = cv2.matchTemplate(small_image, large_image, method)
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)
    MPx,MPy = mnLoc

    trows,tcols = small_image.shape[:2]
    print(f"Top-left corner coordinates: ({MPx}, {MPy})")
    print(f"Bottom-right corner coordinates: ({MPx + tcols}, {MPy + trows})")
    x = (MPx + 20) / 2
    y = (MPy + 20) / 2

    # Move the mouse to the center of the box and click
    print(pyautogui.position())
    pyautogui.moveTo(x, y)
    pyautogui.click()
    pyautogui.click()
    
    # Draw a rectangle around the detected box for testing pruposes
    cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)
    cv2.imwrite('output.png',large_image)
    
if __name__ == '__main__':
    sys.exit(main())