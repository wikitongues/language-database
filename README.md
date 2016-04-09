# Wikitongues Language API 

The language API is a way to centralize all language data across our apps and projects. 

You can find [Poly](https://www.github.com/wikitongues/poly) at [https://www.github.com/wikitongues/poly](https://www.github.com/wikitongues/poly)

You can find the [Oral Histories](https://youtube.com/wikitongues) project on [Youtube](https://youtube.com/wikitongues)

##Description
There are around 7000 languages in the world. With new research emerging all the time, and the boundaries between languages and dialects being frequently challenged and eroded, correctly accounting for this volume and diversity is a world-class data problem.

###The Field of Linguistics
Linguistics is the scientific study of language — its many forms, meanings, and contexts. The field is often said to have emerged in the 4th century BCE, when the Indian grammarian Panini composed a formal description of the Sanskrit language. 

In practice, contemporary linguistic research hones in on a wide scope of nuanced topics, including:

* phonetics (the study of sounds and their perception); 
* semantics (the study of words and their meaning); 
* and pragmatics (the study of the role of context in meaning). 

Linguistics also interacts and co-mingles with other fields of research. 

* Psycholinguistics, for instance, is the study the representation and function of language in the mind, while neurolinguistics explores how brains process language. 
* Computational linguistics applies computer technology to developing models of linguistic knowledge, as well as to create applications for machine translation and language parsing.
* The study of language acquisition seeks to better understand how we learn language, and to improve how we teach it. 
* Sociolinguistics, meanwhile, is the study of the symbiotic relationship between language and society, words and culture. 

Generally speaking, linguistics has a broad potential to help us understand our relationship to the natural world. Lingustics has such a wide array of application because language is the vehicle through which humans understand the world. Language is everything; language is life.

#Current Solution
Wikitongues currently uses a relational spreadsheet service called Airtable to handle all of our language data. You can see a representation [here](https://airtable.com/shrc1ZmAbcrBojRTy/tblm5O4Hj7gnfYYuR).

The language data itself is scraped from the academic repository [Ethnologue](www.ethnologue.com)

#Goal
To build an API that can power Poly not only with external language data, but also to which we can add our own new data in the form of structured dictionaries in the case of Poly, or video as with the Oral Histories. 

##Terms
* ISO
  * The [International Standards Organization](http://www.iso.org/iso/home.html), along with the [Summer Institute for Linguistics](http://www.sil.org/) has devised an ISO code for languages that has seen six revisions so far. Wikitongues uses the third varient, ISO 639-3. Read more on [Wikipedia](https://en.wikipedia.org/wiki/ISO_639) 
* Language Names.
  * Languages sometimes have official names, as well as colloquial or local names. 
  * Has to be an array, as languages necessarily have many names: English, Inglês, 英語
* Writing Systems.
  * There are 125 known writing systems, categorized on [Scriptsource](http://scriptsource.org/cms/scripts/page.php?&id=)
* Genealogy or [Language Family](https://en.wikipedia.org/wiki/Language_family)
  * Genealogy is the historical study of the development of language. How languages change over space and time is encoded in a nesting structure. Ex. [Indo-European] > [Germanic] > ... > [English]. A quick comparisson shows the difference in resolution between [Glottolog](http://glottolog.org/resource/languoid/id/stan1293) and [Ethnologue](https://www.ethnologue.com/subgroups/english-1)
* Demographics
  * Demographic data is often either acquired by linguists on the field or compiled from census data. It is useful in strategizing where to focus our documentation activities.
