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

    // Create an UpdateCursor() method. It will allow the player icon to change with each keypress. Its input will be the key pressed and it will return a symbol that represents the player.
    public new static char UpdateCursor(string key)
    {
      switch (key)
      {
        case "LeftArrow":
          return '<';
        case "RightArrow":
          return '>';
        case "UpArrow":
          return '^';
        case "DownArrow":
          return 'v';
        default:
          return '<';
      }
    }

    // Create a KeepInBounds() method. Without this method, hitting the boundaries will break the game
    public new static int KeepInBounds(int dimension, int max)
    {
      if (dimension < 0)
      {
        return 0;
      }
      else if (dimension >= max)
      {
        return max - 1;
      }
      else 
      {
        return dimension;
      }
    }
  }
}