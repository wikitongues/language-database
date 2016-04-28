#Wikitongues Database
The following concepts were developed during the hackathon hosted by the Recurse Center in New York, USA on April 9th, 2016.

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

###Sample Corpus (English)
|#|Value|Type|Meta|…|
|---|---|---|---|---|
|ID|hello|text||…|
|ID|link/to/resource|video|olá|…|
|…|…|…|…|…|
Each record is a phrase. Phrases can exist in multiple dictionaries or phrase books.

For written languages, you can have both text entries and video entries.

For languages that are not written, video will be used. For video to be indexed by meaning, textual metadata needs to exist. The video meta information will include one of the following:
* if the phrase pair is between text and video, the text is enough to index the video
* if the phrase pair is between video and video, user input will be needed to index the video content.

###Sample Poly User
|#|User Name|OAuth|Books|…|
|---|---|---|---|---|
|ID|Johnathan Swift|Token|[Reference to book table]|…|
|…|…|…|…|

###Book Table ()
|Language 1 ID (`Eng`)|Language 2 ID (`Spa`)|
|---|---|
|Corpus record ID 1|Corpus record ID 2|
|…|…|

#Method 2
Books reference user

###Sample Poly User
|#|User Name|OAuth|…|
|---|---|---|---|
|ID|Vladimir Nabakov|Token|…|
|…|…|…|…|

###Books table
|#|Title|Source language ID|Target language ID|User|…|
|---|---|---|---|---|---|
|ID|Russian for Noobs|`Eng`|`Rus`|Author's ID|…|
|…|…|…|…|…|…|

###Language Pair Corpus
|#|Language 1 ID (`Eng`)|Language 2 ID (`Rus`)|Book ID|…|
|---|---|---|---|---|
|ID|Hello|Привет! (Privyet!)|Book ID|…|
|…|…|…|…|…|

The Language pair corpus or Translation corpus represents all of the phrases that exist between any language pair.

#Method 3
Single universal corpus. In this proposal, dictionaries are aggregates of corpus entries, specified by the interface #.

###Full corpus (phrase list)
|#|Source Language ID|Target Language ID|Source Value| Target Value|Source Type|Target Type|Source Meta|Target Meta|Interface ID|…|
|---|---|---|---|---|---|---|---|---|---|---|
|ID|`Eng`|`Rus`|Hello|Привет! (Privyet!)|Text|Text|…|…|Reference to Book Interface Table|…|
|ID|`Eng`|`Rus`|Hello|link/to/video|Text|Video|…|hello|Reference to Book Interface Table|…|
|…|…|…|…|…|…|…|…|…|…|…|

###Interface Table
|#|Interface #|Book #|…|
|---|---|---|---|
|ID|Interface ID|Book ID|…|
|…|…|…|…|

###Duplicate problem
The following table illustrates a data duplicate problem.

|#|…|Source Value|Target Value|…|
|---|---|---|---|---|
|ID|…|Hello|Привет! (Privyet!)|…|
|ID|…|Привет! (Privyet!)|Hello|…|

Both phrase entries are the same in practice.

##Open questions:
1. To have source and target language ids referenced in both book table and corpus table?
2. How to define source language / target language positions in phrase display?


#Notes:
###ISO 639-3
The [International Standards Organization](http://www.iso.org/iso/home.html), along with the [Summer Institute for Linguistics](http://www.sil.org/) has devised an ISO code for languages that has seen six revisions so far. Wikitongues uses the third varient, ISO 639-3. Read more on [Wikipedia](https://en.wikipedia.org/wiki/ISO_639)
