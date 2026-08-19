*This post is one of a series of articles adapted from my university dissertation on data
visualisation — see the [rest of the series](/blog/tags/datavis-project).*

There are many ways to generate visualisations using any of the languages I have talked about so far,
even some in combination with each other. Sometimes the method and language used is determined by how
the data is stored (e.g. CSV, database, text file, on paper, spreadsheet), or at least some methods
are easier to take from certain formats of data, and sometimes there is more of a free rein, and it
may be down to the developer. Some cases may require a particular language: say if the output must be
done in a particular way, then the choice may be limited or even restricted to one particular
language. If the data is stored in one format and the developer wants to use a particular language, or
has to because they only know one, or the output needs to be in a particular format, then some
conversion processing may need to be done for it to be usable in the chosen environment.

For simple examples on the web, the exact same dynamic output can easily be generated in a number of
ways.

**Example 1 — Number of Friends**

**JavaScript:**

```
<script type="text/javascript">
  var a = window.prompt("How many friends do you have?");
  var b = window.prompt("How many friends does your wife have?");
  ha = a/10;
  hb = b/10;
  sa = ha - 2;
  sb = hb - 2;
  document.write("<div style='width:" + a + "px;height:" + ha + "px;font-size:" + sa + "px;background:red;color:white;padding:5px;font-family:arial;'>YOU</div><br />");
  document.write("<div style='width:" + b + "px;height:" + hb + "px;font-size:" + sb + "px;background:blue;color:white;padding:5px;font-family:arial;'>YOUR PARTNER</div>");
</script>
```

**PHP:**

```
<?php
  $a = $_GET['a'];
  $b = $_GET['b'];
  $ha = $a/10;
  $hb = $b/10;
  $sa = $ha - 2;
  $sb = $hb - 2;
  echo "<div style='width:" . $a . "px;height:" . $ha . "px;font-size:" . $sa . "px;background:red;color:white;padding:5px;font-family:arial;'>YOU</div><br />";
  echo "<div style='width:" . $b . "px;height:" . $hb . "px;font-size:" . $sb . "px;background:blue;color:white;padding:5px;font-family:arial;'>YOUR PARTNER</div>";
?>
```

**PHP embedded in JavaScript:**

```
<script type="text/javascript">
  var a = <?php echo $_GET['a']; ?>
  var b = <?php echo $_GET['b']; ?>
  ha = a/10;
  hb = b/10;
  sa = ha - 2;
  sb = hb - 2;
  document.write("<div style='width:" + a + "px;height:" + ha + "px;font-size:" + sa + "px;background:red;color:white;padding:5px;font-family:arial;'>YOU</div><br />");
  document.write("<div style='width:" + b + "px;height:" + hb + "px;font-size:" + sb + "px;background:blue;color:white;padding:5px;font-family:arial;'>YOUR PARTNER</div>");
</script>
```

All these examples require input of two numbers for comparison and will render a box of colour (red
and blue) to represent each one. The size of the box and the text inside it is determined by the
numbers entered.

<figure class="wp-block-image">
<img src="images/js-prompt-1.webp" />
<img src="images/js-prompt-2.webp" />
<figcaption>JavaScript's prompts</figcaption>
</figure>

The output:

<figure class="wp-block-image">
<img src="images/output-you-vs-partner.webp" />
<figcaption>Visualisation of Your Friends vs. Your Partner's Friends</figcaption>
</figure>
