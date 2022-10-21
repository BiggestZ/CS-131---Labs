import java.awt.Color;
import java.awt.Graphics;

public class Mondrian extends GraphicsObject {

    public Mondrian(int x, int y) {
	super(x, y);
    }

    /* Draw the Mondrian
     *
     * @param g The Graphics for the JPanel
     */
    @Override
    public void draw(Graphics g) {
	// background
	g.setColor(new Color(238, 238, 238));
        g.fillRect(0, 0, 560, 560);

	// borders
	g.setColor(new Color(0, 0, 0));
        g.fillRect(0, 400, 560, 18);
        g.fillRect(120, 0, 18, 560);
        g.fillRect(0, 166, 120, 36);
        g.fillRect(498, 400, 20, 160);
        g.fillRect(518, 473, 42, 25);

	// red
	g.setColor(new Color(222, 42, 34));
        g.fillRect(138, 0, 422, 400);

	// blue
	g.setColor(new Color(4, 92, 164));
        g.fillRect(0, 418, 120, 142);

	// yellow
	g.setColor(new Color(235, 215, 105));
        g.fillRect(518, 497, 42, 63);
    }

}