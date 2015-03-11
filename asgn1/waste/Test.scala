
import java.io._

object Test extends Application
{
       
var myVar = "theValueis";

var myResult="";

myVar match {
       case "someValue"   => myResult= myVar + " A";
       case "thisValue" | "theValueis"   => myResult=myVar + " B";

       case "theValue"    =>  println("Fuck Yeah");
                              myResult=myVar + " C";


       case "doubleValue" => myResult=myVar + " D";
       case _ => println ("Fuck!")
    }
println(myResult);

}


