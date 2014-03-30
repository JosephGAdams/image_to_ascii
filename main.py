# -*- coding: utf-8 -*-
import os
import os.path
import Image
import requests

class code:

    def main(self):
        # Decide which character should be used to represent different shades
        ranges = {'r25': '@', 'r50': '&', 'r75': '%', 'r100': 'a', 'r125': 'c',
        'r150': 'f', 'r175': '!', 'r200': '|', 'r225': ',', 'r250': '.'}
        # Get image url
        url = raw_input('url:')
        # Download image, return file_name, file_extension and file_location
        path = self.create_folder()
        down = self.download_image(url, path)
        # Open image from location
        raw_im = Image.open(os.path.join(down[-1], down[-2]))
        # Make the image smaller, if using a very small image, alter this
        if raw_im.size[0] > 400:
            new_x = raw_im.size[0] / 3
            new_y = raw_im.size[1] / 3
        else:
            new_x = raw_im.size[0]
            new_y = raw_im.size[1]
        im = raw_im.resize((new_x, new_y))
        pix = im.load()
        # image width
        last_x = im.size[0] - 1
        # image height
        last_y = im.size[1] - 1
        # Create text image and save to file
        self.draw_image(down[0], last_x, last_y, pix, ranges)
        
    def create_folder(self):
        base_path = os.getcwd()
        try:
            path = os.mkdir(os.path.join(base_path, "images"), 0777)
        except:
            path = os.path.join(base_path, "images")
        return path
            

    def download_image(self, url, path):
        # Check that image is in correct format
        formats = ['jpg', 'png', 'bmp']
        for each in formats:
            if url.endswith(each):
                # Get url and stream content
                request = requests.get(url, stream=True)
                # Extract filename from url
                filename = url.split('/')[-1].split('.')[0]
                # Extract file_extenios from url
                file_format = url.split('/')[-1].split('.')[-1]
                # Define file_location
                file_loc = "{}.{}".format(filename, file_format)
                # Save file to disk
                print "{}/{}.{}".format(path, filename, file_format)
                with open(path + "/" + filename + '.' + file_format, 'wb') as f:
                    for chunk in request.iter_content(1024):
                        f.write(chunk)
                return (filename, file_format, file_loc, path)
            else:
                pass

    def draw_image(self, filename, last_x, last_y, pix, ranges):
        i, x, y = 0, 0, 0
        # Create a new file using the name gathered above
        f = open(filename + '.txt', 'w')
        # While i is less than the total number of pixels in the image
        while i < last_x * last_y:
            # If x position is not the last in the row
            if x < last_x:
                if x == 0:
                    f.write('|')
                if y == 0:
                    f.write('-')
                # if R in RGB between 0 and 25 write the character designated above to file
                elif pix[x, y][0] in range(0, 25):
                    f.write(ranges['r25'])
                elif pix[x, y][0] in range(25, 50):
                    f.write(ranges['r50'])
                elif pix[x, y][0] in range(50, 75):
                    f.write(ranges['r75'])
                elif pix[x, y][0] in range(75, 100):
                    f.write(ranges['r100'])
                elif pix[x, y][0] in range(100, 125):
                    f.write(ranges['r125'])
                elif pix[x, y][0] in range(125, 150):
                    f.write(ranges['r150'])
                elif pix[x, y][0] in range(150, 175):
                    f.write(ranges['r175'])
                elif pix[x, y][0] in range(175, 200):
                    f.write(ranges['r200'])
                elif pix[x, y][0] in range(200, 225):
                    f.write(ranges['r225'])
                elif pix[x, y][0] in range(225, 256):
                    f.write(ranges['r250'])
                x += 1
            # if x is the last in the row, write the last character and then start a new line
            elif x == last_x:
                f.write('|\n')
                x = 0
                y += 1
            i += 1
        print os.path.abspath(filename + '.txt')

if __name__ == "__main__":
    code().main()