import json
import cv2
import os


class DataParser:
    """A class for parsing data from JSON to CSV and preprocessing images."""

    def __init__(self):
        """Initializes the DataParser class."""
        self.length = 1  # It's not clear what `length` is for. You may want to add a comment or remove it.

    def jsonToCsv(self, jsonName: str, csvName: str = "object_map.csv"):
        """
        Converts JSON data to CSV format.

        Parameters:
            jsonName (str): The path to the input JSON file.
            csvName (str): The path to the output CSV file. Defaults to "object_map.csv".
        """
        output_lines = []
        output_lines.append("xmin,ymin,xmax,ymax,Object,label")

        with open(jsonName, 'r') as f:
            json_data = json.load(f)

        for entry in json_data:
            for key, value in entry.items():
                coordinates = value['coordinates']
                xmin, ymin, xmax, ymax = coordinates
                obj_value = value['value']
                label = value['label']
                output_line = f"{xmin},{ymin},{xmax},{ymax},{obj_value},{label}"
                output_lines.append(output_line)

        with open(csvName, "w") as f:
            for line in output_lines:
                f.write(line + "\n")

    def preprocessImage(self, imageName: str, outputName: str = "gray_image.jpg"):
        """
        Preprocesses an image by converting it to grayscale.

        Parameters:
            imageName (str): The path to the input image.
            outputName (str): The path to the output grayscale image. Defaults to "gray_image.jpg".
        """
        if not os.path.exists(imageName):
            print(f"The file {imageName} does not exist.")
            return

        image = cv2.imread(imageName)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(outputName, gray_image)
        cv2.imshow('Grayscale Image', gray_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def grayToRGB(self, grayImageName: str, outputName: str = "rgb_image.jpg"):
        """
        Converts a grayscale image to an RGB image.

        Parameters:
            grayImageName (str): The path to the input grayscale image.
            outputName (str): The path to the output RGB image. Defaults to "rgb_image.jpg".
        """
        # Read the grayscale image
        gray_image = cv2.imread(grayImageName, cv2.IMREAD_GRAYSCALE)

        # Convert grayscale to RGB
        rgb_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)

        # Save the RGB image
        cv2.imwrite(outputName, rgb_image)

        # Show the RGB image
        cv2.imshow('RGB Image', rgb_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    my_data_parser = DataParser()
    # my_data_parser.preprocessImage('wa_filled_0.jpeg', 'wa_ticket_gr.jpg')
    my_data_parser.grayToRGB('wa_filled_0.jpeg')
