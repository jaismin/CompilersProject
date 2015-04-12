class Point(val xc: Int, val yc: Int) {
   val x: Int = xc;
   val y: Int = yc;
   def move(dx: Int, dy: Int):Unit = {
      x = x + dx;
      y = y + dy;
      // println ("Point x location : " + x);
      // println ("Point y location : " + y);
   }
}

// class Location(val xc: Int,val yc: Int,val zc :Int) {
//    var z: Int = zc;

//    def move(dx: Int, dy: Int, dz: Int):Int = {
//       x = x + dx;
//       y = y + dy;
//       z = z + dz;
//       // println ("Point x location : " + x);
//       // println ("Point y location : " + y);
//       // println ("Point z location : " + z);
//       return x;
//    }
// }

object Test {
   def main(args: Array[String]):String = {
      val loc:Point = new Point(10, 20);

      // Move to a new location
      loc.move(10, 10);
      return "Hello"+"World";
   }
}