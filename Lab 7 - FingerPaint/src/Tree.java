import java.awt.Color;
import java.awt.Graphics;
import java.util.Random;

public class Tree extends GraphicsObject{
    int radius;
    Color color;
    int TreeW;
    int TreeH;
    int closeness;
    Color TreeClr;

    public Tree(int x, int y, int radius, Color color, int TreeW, int TreeH, int closeness, Color TreeClr) {
        super(x, y); //x and y is not explicitly declare because Rectangle class extends GraphicsObject (Super class)
        this.radius = radius;
        this.color = color;
        this.TreeW = TreeW;
        this.TreeH = TreeH;
        this.closeness = closeness;
        this.TreeClr = TreeClr;
    }

    @Override

    public void draw(Graphics g) {

        //draw tree trunk
        //int ex = x - closness;
        //int ey = y + closness; //- vrejHeight;
        g.setColor(TreeClr);
        g.fillRect(x - closeness, y + closeness, TreeW, TreeH);

        //draw circle
        g.setColor(this.color);
        int diameter = radius * 2;
        g.fillOval(x - radius, y - radius, diameter, diameter);

    }
}
