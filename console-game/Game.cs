using System;

namespace ConsoleGame
{
  class Game : SuperGame
  {

    // Create a switch statement inside an UpdatePosition() method. This method will be used to change the position of the character based on keyboard input.
    public new static void UpdatePosition(string key, out int xChange, out int yChange)
    {
      switch (key)
      {
        case "LeftArrow":
          xChange = -1;
          yChange = 0;
          break;
        case "RightArrow":
          xChange = 1;
          yChange = 0;
          break;
        case "UpArrow":
          xChange = 0;
          yChange = -1;
          break;
        case "DownArrow":
          xChange = 0;
          yChange = 1;
          break;
        default:
        	xChange = 0;
          yChange = 0;
          break;
      }
    }
  }
}