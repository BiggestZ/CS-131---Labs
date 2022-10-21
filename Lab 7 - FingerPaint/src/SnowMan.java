import java.awt.Color;
import java.awt.Graphics;

public class SnowMan extends GraphicsObject {
    //Dimensions of Body
    int width;
    int height;
    //Dimensions of 2nd body
    Color color;
    Color black = new Color(0,0,0);

    public SnowMan (int x, int y, int width, int height, Color color){
        super(x, y);
        this.width = width;
        this.height = height;
        this.color = color;
    }

    @Override //Syntax to Override the draw class from Graphics Object
    public void draw(Graphics g) {
        g.setColor(this.color);
        g.fillOval(this.x, this.y, this.width/2, this.height/2); //Draw the bottom
        g.setColor(black);
        g.drawOval(this.x, this.y, this.width/2, this.height/2); //Black Outline
        
        //Draw Midsection
        g.setColor(this.color);
        g.fillOval(this.x+16, this.y - 25, this.width / 3, this.height / 3);
        g.setColor(black);
        g.drawOval(this.x+16, this.y - 25, this.width / 3, this.height / 3);

        // Draw Head
        g.setColor(this.color);
        g.fillOval(this.x + 25, this.y - 60, this.width / 4, this.height / 4);
        g.setColor(black);
        g.drawOval(this.x + 25, this.y - 60, this.width / 4, this.height / 4);
    }
} //COMPLETE

    
