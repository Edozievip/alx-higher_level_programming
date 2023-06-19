#!/usr/bin/node
// this is rectangle class with two arguements

class Rectangle {
    constructor (w, h) {
      if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
      }
    }
  }
  
  module.exports = Rectangle;
  