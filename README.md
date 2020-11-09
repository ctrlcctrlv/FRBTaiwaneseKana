<!-- pandoc -f markdown -t html -i README.md -o README.html -->

<!-- Only works w/Pandoc, not in GitHub where it's ignored. -->
<!--<style>
    @font-face {
        font-family: "FRBTaiwaneseKana2";
        src: url("./FRBTaiwaneseKana.otf");
    }
    table {
        border-collapse: collapse
    }
    table, th, td {
        border: 1px solid black
    }
    table.tkana td {
        font-family: "FRBTaiwaneseKana2", "Noto Serif CJK TC", serif;
        font-size: 2em
    }
    th, td {
        padding: 5px
    }
</style>-->

# FRB Taiwanese Kana

<!-- To make specimen; print to PDF in Firefox (landscape), then :
     gm convert -density 400 specimen.pdf +adjoin specimen-%0d.png -->
     
![](https://raw.githubusercontent.com/ctrlcctrlv/FRBTaiwaneseKana/master/specimen-0.png)
![](https://raw.githubusercontent.com/ctrlcctrlv/FRBTaiwaneseKana/master/specimen-1.png)

This is a Taiwanese kana font, originally meant to accompany my Unicode proposal, *A proposal to encode Taiwanese kana in the UCS*.

It supports vertical layout, ruby, and all of the Taiwanese kana. 

## Tone letters

Table starts at U+1AFF0.

<table>
<tr><th>0</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th></tr>
<tr><td>Tone 2</td><td>Tone 3</td><td>Tone 4</td><td>Tone 5</td><td>-</td><td>Tone 7</td><td>Tone 8</td></tr>
<tr><th colspan=8>Nasalized</th></tr>
<tr><th>7</th><th>8</th><th>9</th><th>A</th><th>B</th><th>C</th><th>D</th><th>E</th><th>F</th></tr>
<tr><td>Tone 1</td><td>Tone 2</td><td>Tone 3</td><td>Tone 4</td><td>Tone 5</td><td>-</td><td>Tone 7</td><td>Tone 8</td><td>-</td></tr>
</table>

----

<table class="tkana">
<tr><th>0</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th></tr>
<tr><td>&#x1aff0;</td><td>&#x1aff1;</td><td>&#x1aff2;</td><td>&#x1aff3;</td><td>-</td><td>&#x1aff5;</td><td>&#x1aff6;</td><td>&#x1aff7;</td></tr>
<tr><th>8</th><th>9</th><th>A</th><th>B</th><th>C</th><th>D</th><th>E</th><th>F</th></tr>
<tr><td>&#x1aff8;</td><td>&#x1aff9;</td><td>&#x1affa;</td><td>&#x1affb;</td><td>-</td><td>&#x1affd;</td><td>&#x1affe;</td><td>-</td></tr>
</table>

The codepoints it uses are subject to change; see also [the draft Unicode proposal](https://raw.githubusercontent.com/ctrlcctrlv/TaiwaneseKanaUnicodePaper/master/tkana.pdf).

