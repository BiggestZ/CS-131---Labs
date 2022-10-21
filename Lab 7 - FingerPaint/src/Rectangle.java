import java.awt.Color;
import java.awt.Graphics;

public class Rectangle extends GraphicsObject {

    int width;
    int height;
    Color color;

    public Rectangle(int x, int y, int width, int height, Color color) {
        super(x, y); // X and Y are there because the class is an extension of GraphicsObject
        // super(x, y) grabs the x and y from the GraphicsObject class
        this.width = width;
        this.height = height;
        this.color = color;
    }

    /* Draw the rectangle
     *
     * @param g The Graphics for the JPanel
     */
    @Override //Syntax to Override the draw class from Graphics Object
    public void draw(Graphics g) {
        // change the color of the pen
        g.setColor(this.color);
        // draw the rectangle
        g.fillRect(this.x, this.y, this.width, this.height);
    }

}