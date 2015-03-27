object Test {
   def main(args: Array[String]): Unit = {
      var x:Double = 10.0;

      if( x == 10 ){
         println("Value of X is 10");
      }else if( x == 20 ){
         println("Value of X is 20");
      }else if( x == 30 ){
         println("Value of X is 30");
      }else{
         println("This is else statement");
      }

      while( true ){
         println( "Value of a: " + a );
      }

      var a:Int = 10;

      // do loop execution
      do{
         println( "Value of a: " + a );
         a = a + 1;
      }while( a < 20 );

      var a:Int = 0;
      var b:Int = 0;
      // for loop execution with a range
      for( a <- 1 to 3; b <- 1 to 3){
         println( "Value of a: " + a );
         println( "Value of b: " + b );
      }

   }
}