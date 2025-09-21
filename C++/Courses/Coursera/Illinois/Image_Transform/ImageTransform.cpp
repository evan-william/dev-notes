#include <iostream>
#include <cmath>
#include <cstdlib>

#include "uiuc/PNG.h"
#include "uiuc/HSLAPixel.h"
#include "ImageTransform.h"

/* ******************
(Begin multi-line comment...)

Write your name and email address in the comment space here:

Name: John Doe
Email: example@example.com

(...end multi-line comment.)
******************** */

using uiuc::PNG;
using uiuc::HSLAPixel;

/**
 * Returns an image that has been transformed to grayscale.
 *
 * The saturation of every pixel is set to 0, removing any color.
 *
 * @return The grayscale image.
 */
PNG grayscale(PNG image) {
  /// This function is already written for you so you can see how to
  /// interact with our PNG class.
  for (unsigned x = 0; x < image.width(); x++) {
    for (unsigned y = 0; y < image.height(); y++) {
      HSLAPixel & pixel = image.getPixel(x, y);

      // `pixel` is a reference to the memory stored inside of the PNG `image`,
      // which means you're changing the image directly. No need to `set`
      // the pixel since you're directly changing the memory of the image.
      pixel.s = 0;
    }
  }

  return image;
}

/**
 * Returns an image with a spotlight centered at (`centerX`, `centerY`).
 *
 * A spotlight adjusts the luminance of a pixel based on the distance the pixel
 * is away from the center by decreasing the luminance by 0.5% per 1 pixel euclidean
 * distance away from the center.
 *
 * For example, a pixel 3 pixels above and 4 pixels to the right of the center
 * is a total of `sqrt((3 * 3) + (4 * 4)) = sqrt(25) = 5` pixels away and
 * its luminance is decreased by 2.5% (0.975x its original value).  At a
 * distance over 160 pixels away, the luminance will always decreased by 80%.
 * 
 * The modified PNG is then returned.
 *
 * @param image A PNG object which holds the image data to be modified.
 * @param centerX The center x coordinate of the crosshair which is to be drawn.
 * @param centerY The center y coordinate of the crosshair which is to be drawn.
 *
 * @return The image with a spotlight.
 */
PNG createSpotlight(PNG image, int centerX, int centerY) {
  for (unsigned x = 0; x < image.width(); x++) {
    for (unsigned y = 0; y < image.height(); y++) {
      HSLAPixel & pixel = image.getPixel(x, y);
      
      // Calculate Euclidean distance
      double distance = sqrt(pow(x - centerX, 2) + pow(y - centerY, 2));
      
      // Decrease luminance based on distance
      // 0.5% decrease per pixel distance, up to 80% maximum decrease
      double decrease_factor = 0.005 * distance;
      if (decrease_factor > 0.8) {
        decrease_factor = 0.8;
      }
      
      // Apply the decrease
      pixel.l = pixel.l * (1 - decrease_factor);
    }
  }
  return image;
}

/**
 * Returns a image transformed to Illini colors.
 *
 * The hue of every pixel is set to the a hue value of either orange or
 * blue, based on if the pixel's hue value is closer to orange than blue.
 *
 * @param image A PNG object which holds the image data to be modified.
 *
 * @return The illinify'd image.
**/
PNG illinify(PNG image) {
  // Illini orange and blue hue values
  const double ILLINI_ORANGE = 11;
  const double ILLINI_BLUE = 216;
  
  for (unsigned x = 0; x < image.width(); x++) {
    for (unsigned y = 0; y < image.height(); y++) {
      HSLAPixel & pixel = image.getPixel(x, y);
      
      // Calculate the distance to orange and blue hues
      double dist_to_orange = std::min(abs(pixel.h - ILLINI_ORANGE), 360 - abs(pixel.h - ILLINI_ORANGE));
      double dist_to_blue = std::min(abs(pixel.h - ILLINI_BLUE), 360 - abs(pixel.h - ILLINI_BLUE));
      
      // Set hue to the closer of orange or blue
      if (dist_to_orange <= dist_to_blue) {
        pixel.h = ILLINI_ORANGE;
      } else {
        pixel.h = ILLINI_BLUE;
      }
    }
  }
  
  return image;
}

/**
* Returns an immge that has been watermarked by another image.
*
* The luminance of every pixel of the second image is checked, if that
* pixel's luminance is 1 (100%), then the pixel at the same location on
* the first image has its luminance increased by 0.2.
*
* @param firstImage  The first of the two PNGs, which is the base image.
* @param secondImage The second of the two PNGs, which acts as the stencil.
*
* @return The watermarked image.
*/
PNG watermark(PNG firstImage, PNG secondImage) {
  // Get the minimum width and height
  unsigned int min_width = std::min(firstImage.width(), secondImage.width());
  unsigned int min_height = std::min(firstImage.height(), secondImage.height());
  
  // For each pixel that exists in both images
  for (unsigned x = 0; x < min_width; x++) {
    for (unsigned y = 0; y < min_height; y++) {
      HSLAPixel & first_pixel = firstImage.getPixel(x, y);
      HSLAPixel & second_pixel = secondImage.getPixel(x, y);
      
      // If the second image's pixel luminance is at maximum (1.0)
      if (second_pixel.l == 1.0) {
        // Increase the luminance of the first image by 0.2
        // but don't exceed the maximum of 1.0
        first_pixel.l = std::min(first_pixel.l + 0.2, 1.0);
      }
    }
  }
  
  return firstImage;
}