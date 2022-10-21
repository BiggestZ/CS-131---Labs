import java.awt.Color;
import java.awt.Graphics;

public class Background extends GraphicsObject{
    int height;
    Color color;
    Color black = new Color(0,0,0);
    Color white = new Color(255,255,255);

    public Background (int x, int y, Color color){
        super(x, y);
        this.height = 560-y;
        this.color = color;
    }

    @Override //Syntax to Override the draw class from Graphics Object
    public void draw(Graphics g) {
        // change the color of the pen
        g.setColor(black);
        // draw the sky
        g.fillRect(0,0,560,560);
        
        g.setColor(this.color); //Color of ground

        g.fillRect(this.x, this.y, 560, this.height); //Ground
    }

} //Complete
