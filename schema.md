#Wikitongues Database
The following concepts were developed during the hackathon hosted by the Recurse Center in New York, USA on April 9th, 2016.
##Basic terms
* ####Phrase

   Text or video unit
* ####Phrase pair

   Relationship between phrases implying translation between two languages
* ####Dictionary

   Collection of phrase pairs
* ####Book

   Container for dictionary with extra user metadata such as titles, descriptions, authorship etc...

##Index table
The index table accounts for all languages in the world.

|ID|Names|…|
|---|:---:|---|
|`ENG`|[English, Inglês, Anglais,…]|…|
|`CMN`|[Chinese (Mandarin), Beifang Fangyan, Guanhua,…]|…|
|…|…|…|
For language names, an array of all of the strings used in naming a language

#Method 1
Each language has a corpus table with all of the phrases in that language. Each user owns their authored books.
###User Table
|ID|User Name|Books|…|
|---|---|---|---|
|#|Johnathan Swift|[Reference to book table]|…|
|…|…|…|
###Book Table
Each book would have it's own table defining which phrases it owns

|Language 1 ID (`Eng`)|Language 2 ID (`Spa`)|
|---|---|
|Record #|Record #|
|…|…|

We know which language corpus to refer to by the table headers.

I wonder if the book reference on the user table couldnt be something along the lines of [{eng:spa,{english corpus record #:spanish corpus record #, english corpus record #:spanish corpus record #}}]
###`Eng` Corpus
|ID|Value|Type|Meta|…|
|---|---|---|---|---|
|#|hello|text||…|
|#|link/to/resource|video|olá|…|
|…|…|…|…|…|
Each record is a phrase. Phrases can exist in multiple dictionaries or phrase books.

For written languages, you can have both text entries and video entries.

For languages that are not written, video will be used. For video to be indexed by meaning, textual metadata needs to exist. The video meta information will include one of the following:
* if the phrase pair is between text and video, the text is enough to index the video
* if the phrase pair is between video and video, user input will be needed to index the video content.

#Method 2
A centralized books table references each author. Each language pair has its own unique corpus table.
###User Table
|ID|User Name|OAuth|…|
|---|---|---|---|
|#|Vladimir Nabakov|Token|…|
|…|…|…|…|
###Books table
|ID|Title|Source language ID|Target language ID|User|…|
|---|---|---|---|---|---|
|#|Russian for Noobs|`Eng`|`Rus`|Author's ID|…|
|…|…|…|…|…|…|
###Language Pair Corpus
|ID|Language 1 ID (`Eng`)|Language 2 ID (`Rus`)|Book ID|…|
|---|---|---|---|---|
|#|Hello|Привет! (Privyet!)|Book ID|…|
|…|…|…|…|…|
The Language pair corpus or Translation corpus represents all of the phrases that exist between any language pair.

Downsides: 7000^7000 = 49 million language pairs. Outrage.
#Method 3
Single universal corpus. In this proposal, dictionaries are aggregates of corpus entries, specified by the interface #.
###Full corpus (phrase list)
|ID|Source Lang ID|Target Lang ID|Source Value| Target Value|Source Type|Target Type|Source Meta|Target Meta|Interface ID|…|
|---|---|---|---|---|---|---|---|---|---|---|
|#|`Eng`|`Rus`|Hello|Привет! (Privyet!)|Text|Text|…|…|Reference to Book Interface Table|…|
|#|`Eng`|`Rus`|Hello|link/to/video|Text|Video|…|hello|Reference to Book Interface Table|…|
|…|…|…|…|…|…|…|…|…|…|…|
###Interface Table
|ID|Interface #|Book #|…|
|---|---|---|---|
|#|Interface ID|Book ID|…|
|…|…|…|…|
###Duplicate problem
The following table illustrates a data duplicate problem.

|ID|…|Source Value|Target Value|…|
|---|---|---|---|---|
|#|…|Hello|Привет! (Privyet!)|…|
|#|…|Привет! (Privyet!)|Hello|…|
Both phrase entries are the same in practice.
##Open questions:
1. To have source and target language ids referenced in both book table and corpus table?
2. How to define source language / target language positions in phrase display?

#Notes:
###ISO 639-3
The [International Standards Organization](http://www.iso.org/iso/home.html), along with the [Summer Institute for Linguistics](http://www.sil.org/) has devised an ISO code for languages that has seen six revisions so far. Wikitongues uses the third varient, ISO 639-3. Read more on [Wikipedia](https://en.wikipedia.org/wiki/ISO_639)
