/**
 * @file HSLAPixel.h
 * Definition of the HSLAPixel class for use with the PNG library.
 *
 * @author CS 225 Course Staff
 * @version 2018r1-lab1
 */

#pragma once

namespace uiuc {
  /**
   * Represents a color in HSLA space.
   */
  class HSLAPixel {
  public:
    double h; // Hue of the pixel, in degrees [0, 360)
    double s; // Saturation of the pixel, [0, 1]
    double l; // Luminance of the pixel, [0, 1]
    double a; // Alpha (transparency) of the pixel, [0, 1]
  };
}