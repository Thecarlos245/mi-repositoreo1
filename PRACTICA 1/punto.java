
// clase Punto
public class punto {
    public float x;
    public float y;
    
public punto(float x, float y){
this.x = x;
this.y = y;
}

public float[] coord_cartesianas() {
 return new float[] {this.x, this.y};
}
public float[] coord_polares() {
 float radio = (float)Math.sqrt(this.x * this.x + this.y * this.y);
 float angulo = (float) Math.atan(this.y/this.y);
 angulo = (float) Math.toDegrees(angulo);
 return new float[] {radio, angulo};
}
public String toString(){
return String.format("(%.2f, %.2f)", this.x, this.y);
}


    
}
// clase Principal 
public class Tarea1 {

    public static void main(String[] args) {
        // TODO code application logic here
        punto p1 = new punto(0,3);
System.out.println(p1);
float a[] = p1.coord_cartesianas();
System.out.println(a[0] + " " + a[1]);
float b[] = p1.coord_polares();
System.out.println(b[0] + " " + b[1]);
    }
    
}
