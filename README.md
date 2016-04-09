# Wikitongues Language API 

The language API is a way to centralize all language data across our apps and projects. 

You can find [Poly](https://www.github.com/wikitongues/poly) at [https://www.github.com/wikitongues/poly](https://www.github.com/wikitongues/poly)

You can find the [Oral Histories](https://youtube.com/wikitongues) project on [Youtube](https://youtube.com/wikitongues)

###Description
There are around 7000 languages in the world. With new research emerging all the time, and the boundaries between languages and dialects being frequently challenged and eroded, correctly accounting for this volume and diversity is a world-class data problem.

###The Field of Linguistics
ethonologue data structure
glottolog

##Problems
* Language data resolution is constantly challenged.
* multiple language names
* dialects
* Different data structures
* 

#Current Solution
Wikitongues currently uses a relational spreadsheet service called Airtable to handle all of our language data. 
The language data itself is scraped from the academic repository [Ethnologue](www.ethnologue.com)

##Terms
* ISO
  * The [International Standards Organization](http://www.iso.org/iso/home.html), along with the [Summer Institute for Linguistics](http://www.sil.org/) has devised an ISO code for languages that has seen six revisions so far. Wikitongues uses the third varient, ISO 639-3. Read more on [Wikipedia](https://en.wikipedia.org/wiki/ISO_639) 
* Language Names.
  * Languages sometimes have official names, as well as colloquial or local names. 
  * Has to be an array, as languages necessarily have many names: English, Inglês, 英語
* Writing Systems.
  * There are 125 known writing systems, categorized by [Scriptsource](http://scriptsource.org/cms/scripts/page.php?&id=)
* Genealogy or [Language Family](https://en.wikipedia.org/wiki/Language_family)
  * Genealogy is the historical study of the development of language. How languages change over space and time is encoded in a nesting structure. Ex. [Indo-European] > [Germanic] > ... > [English]
* Demographics
  * Demographic data is often either acquired by linguists on the field or compiled from census data. It is useful in strategizing where to focus our documentation activities.
