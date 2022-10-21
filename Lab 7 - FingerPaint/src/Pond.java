import java.awt.Color;
import java.awt.Graphics;

public class Pond extends GraphicsObject{ // A strecthed ellipse
    int width;
    int height;
    Color color;
    Color black = new Color(0,0,0);

    public Pond(int x, int y, int width, int height, Color color){
        super(x,y);
        this.width = width;
        this.height = height;
        this.color = color;
    }

    @Override //Syntax to Override the draw class from Graphics Object
    public void draw(Graphics g) {
        // change the color of the pen
        g.setColor(this.color);
        // draw the rectangle
        g.fillOval(this.x, this.y, this.width, this.height);

        g.setColor(black);
        g.drawOval(this.x, this.y, this.width, this.height);
        
    }

}
