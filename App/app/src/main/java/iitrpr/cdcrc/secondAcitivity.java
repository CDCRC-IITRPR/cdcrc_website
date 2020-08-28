package iitrpr.cdcrc;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;

public class secondAcitivity extends AppCompatActivity {
    boolean isOpen=false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        //set up full screen
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,WindowManager.LayoutParams.FLAG_FULLSCREEN);
        setContentView(R.layout.second_main);
    }


    public void openHome(View view) {
        Intent intent=new Intent(this,MainActivity.class);
        startActivity(intent);
    }

    public void openFacebook(View view) {
        Uri uri = Uri.parse("https://www.facebook.com/Career-Development-Corporate-Relations-Center-IIT-Ropar-169217773601805/"); // missing 'http://' will cause crashed
        Intent intent = new Intent(Intent.ACTION_VIEW, uri);
        startActivity(intent);
    }

    public void openInsta(View view) {
        Uri uri = Uri.parse("https://www.instagram.com/"); // missing 'http://' will cause crashed
        Intent intent = new Intent(Intent.ACTION_VIEW, uri);
        startActivity(intent);
    }

    public void openLinked(View view) {
        Uri uri = Uri.parse("https://in.linkedin.com/in/iit-ropar-training-and-placement-cell-347a1a66"); // missing 'http://' will cause crashed
        Intent intent = new Intent(Intent.ACTION_VIEW, uri);
        startActivity(intent);
    }

    public void openTwitter(View view) {
        Uri uri = Uri.parse("https://twitter.com/T_PCell_IITRPR"); // missing 'http://' will cause crashed
        Intent intent = new Intent(Intent.ACTION_VIEW, uri);
        startActivity(intent);
    }

    public void openAboutus(View view) {
        Uri uri = Uri.parse("http://www.iitrpr.ac.in/TP/"); // missing 'http://' will cause crashed
        Intent intent = new Intent(Intent.ACTION_VIEW, uri);
        startActivity(intent);
    }

    public void openStudents(View view) {
        Uri uri = Uri.parse("http://www.iitrpr.ac.in/TP/index.php/contact-us/"); // missing 'http://' will cause crashed
        Intent intent = new Intent(Intent.ACTION_VIEW, uri);
        startActivity(intent);
    }
}