import java.awt.Color;
import java.awt.Graphics;

public class Stars extends GraphicsObject{ //Circles in the sky, multiple and random
    int width;
    int height;
    Color color;

    public Stars (int x, int y, int width, int height, Color color) {
        super(x,y);
        this.width = width;
        this.height = height;
        this.color = color;
    }

    public void draw(Graphics g) {
        g.setColor(this.color);
        g.fillOval(this.x, this.y, this.width, this.height);


    }
} //Complete
