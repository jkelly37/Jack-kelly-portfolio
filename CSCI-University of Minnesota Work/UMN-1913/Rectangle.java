import java.math.*;

public class Rectangle extends Polygon {
    public Rectangle( int side1, int side2){
        super(4,side1,side2,side1,side2);

    }

    public int getArea(){
        return side(1) * side(2);

    }

    public double getDiagonal(){
        return(Math.sqrt(Math.pow(side(1),2) + Math.pow(side(2),2)));

    }

    public boolean fitsInside(Rectangle r2){
        if(( r2.getDiagonal() < this.side(1)&& ( r2.side(2) < this.side(2)))) {
            return true;
        }
        if(( r2.side(2) < this.side(1)&& ( r2.side(1) < this.side(2)))) {
            return true;
        }
        return false;
    }



}
