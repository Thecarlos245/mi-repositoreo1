

import javax.swing.*;
import java.awt.*;

// Clase Punto
class Punto {
    float x, y;

    public Punto(float x, float y) {
        this.x = x;
        this.y = y;
    }
}

// Clase Circulo 
class Circulo extends JPanel {
    Punto centro;
    float radio;

    public Circulo(Punto c, int r) {
        this.centro = c;
        this.radio = r;
        setPreferredSize(new Dimension(400, 400)); // Tamaño del panel
    }

    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.setColor(Color.RED);
        g.drawOval(centro.x*10, centro.y*10, 2 * radio * 10, 2 * radio * 10);
    }

    // Método para mostrar el círculo en una ventana
    public void mostrar() {
        JFrame frame = new JFrame("Dibujar Círculo");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(this);
        frame.pack();
        frame.setVisible(true);
    }
}

// Clase principal
public class GraficoCirculo {
    public static void main(String[] args) {
        Punto centro = new Punto(2, 2);
        float radio = 5;
        Circulo circulo = new Circulo(centro, radio);
        circulo.mostrar(); 
    }
}
