// utility stuff
import java.util.ArrayList;
import java.util.Random;

// graphics stuff
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;

//Main File where code is run, pictures are made.

public class Picture extends JPanel {
    private int canvasWidth;
    private int canvasHeight;

    private ArrayList<GraphicsObject> objects; //A list that will hold all the objects

    /* Constructor for a window/canvas of a specified size
     *
     * @param width  The width of the canvas.
     * @param height The height of the canvas.
     */
    public Picture(int width, int height) {
	this.canvasWidth = width;
	this.canvasHeight = height;
	this.objects = new ArrayList<GraphicsObject>();
    }

    /* Creates the window and shows it
     */
    public void showCanvas() {
	JFrame frame = new JFrame("Picture");
	frame.getContentPane().add(this, BorderLayout.CENTER);
	frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	Dimension dim = new Dimension(this.canvasWidth, this.canvasHeight);
	frame.getContentPane().setPreferredSize(dim);
	frame.pack();
	frame.setVisible(true);
    }

    /* Convenience function to paint all objects.
     */
    public void paint() {
	this.paint(this.getGraphics());
    }

    /* Paint/Draw the canvas.
     *
     * This function overrides the paint function in JPanel. This function is
     * automatically called when the panel is made visible.
     *
     * @param g The Graphics for the JPanel
     */
    @Override
    public void paint(Graphics g) {
	// use a for-each loop to draw each object
	for (GraphicsObject obj : this.objects) {
	    obj.draw(g);
	}
    }

    /* Add an object to be draw.
     *
     * @param obj The object to draw.
     */
    public void addObject(GraphicsObject obj) {
	this.objects.add(obj);
    }

    private static int getRandomNumberInRange(int min, int max) {

		if (min >= max) {
			throw new IllegalArgumentException("max must be greater than min");
		}

		Random r = new Random();
		return r.nextInt((max - min) + 1) + min;
	}

    public static void main(String[] args) {
	// make a picture that is 560x560 pixels
	Picture pic = new Picture(560, 560);

	// FIXME Add the objects for your picture here
	//pic.addObject(new Rectangle(0, 0, 560, 560, new Color(0, 0, 0)));
	//pic.addObject(new Rectangle(100, 150, 50, 50, new Color(154, 8, 178)));
	//pic.addObject(new Rectangle(300, 300, 150, 100, new Color(255, 255, 255)));

	// for something more complicated, uncomment the next line
	//pic.addObject(new Mondrian(0, 0));
    //pic.addObject(new Rectangle(0, 0, 560, 560, new Color(0, 0, 0))); // Sky
    
    
    pic.addObject(new Background(0, 380, new Color(0, 128 ,0))); // Ground + Sky

    for( int i = 0; i < 50; i++ ) {
    pic.addObject(new Stars(getRandomNumberInRange(0, 560),getRandomNumberInRange(0, 260), 10, 10 ,new Color(240,230,140))); //For Loop 10, range sizes
    }
    pic.addObject(new SnowMan(30, 320, 200 , 200, new Color(255,255,255))); //Only 1
	
    pic.addObject(new Pond(100, 450, 150 , 50, new Color(70,130,180))); //Only 1

    pic.addObject(new Tree(420,310, 80, new Color(0,100,0),40,120,20,new Color(139,69,19)));

    pic.showCanvas();
	pic.paint();
    }

}