FORMAT: .1

# WID - Lemma<sup>[1](#footnote1)</sup> reference engine

We are defining an API to be used for creating and retrieving associations between given words in a language-agnostic context. The first use of this service will be the population and retrieval of language names.

The API will expose a single resource, called a `Reference`. A reference has 4 components:

- Sign *(think of it as the content string)*
- Domain *(effectively a language scope)*
  * Referent *(scope in different language)* `!F not sure if this should be representationally nested`
- Context/Host language *(system or interface language)*

Roughly speaking, these express the following statement: 

`In [Context language W], [Sign X] means [Referent Y] in [Domain Z]`

Ex: In the [`Context language`:`English`], the [`Sign`:`French`] means the [`Referent`:`Francês`] in the [`Domain`:`Portuguese`]

The `Referent` is an integral part of a reference statement but remains internal to the system.

The system can be expressed as a series of `References` of this form.

### Sign

A `Sign` is a *content object*<sup>[2](#footnote2)</sup>. It is the realization`! confusing word` of a `Referent` within a given `Domain`. In the context of human language, it is a vocabulary element.


### Domain

A `Domain` is also a *content object*, representing the scope within which an associated `Sign` is valid. 

In the context of human language, it is the name of the language that possesses the desired vocabulary element `X`. 

Because: 

1. the set of languages is neither fixed nor known
2. the system cannot privilege any particular linguistic expression of any entity

the `Domain` element is as dynamic and provisional as the sign element. 

`!F a domain seems to be a sign with priviledges`


### Referent

Every entity or "object" in the system is represented by a single `Referent`. Multiple statements with the same referent will be understood to have a *translational* relationship; that is, to be realizations of the same referent in their respective domains. 

However, the `Referent` is a bare identifier without any semantic meaning of its own, and doesn't privilege any given form of expression. Therefore any reference to a `Referent` entity will necessarily be through one of its representations; the client cannot invoke an object directly.

The initial population will be the known human languages, as indexed on [Ethnologue](ethnologue.com/).

### Context/Host language

The `Context language` is the namespace for a `Reference`. Every interaction with the system will necessarily be in a known `Context language`. For instance, take the interface language of the application during a user session. 

If a `Context language` contains a statement about a given domain, that statement will be 'in scope' within that context; however, the statement may also be in scope in other contexts without explicitly expressed statements. 

`!F confusing; unclear scopes, contexts, statements`

`!F how so? Needing to know this, or inferring meaning from this seems like it makes the system more rigid. Can we not leverage the well-defined structure of phrase pairs, with defined source and target languages, and remove the outmost layer`

Ex: if a non-Latin context language like Arabic contains a statement about the English word "donkey" (transliterated, presumably, in Arabic characters), that statement will be accessible in any query on English from within the context. But a statement about the English word "donkey" in the English context, rendered normally, will in all likelihood be available in other Latin-alphabet contexts, without it needing to be repeatedly established that the English word is "donkey". `!F not sure what you mean here`

Ex: The following **false** proposition, expressed in the `Context language` `English`, claims that the `Sign` `Français` means the `Referent` `Francês` in the `Domain` `Portuguese`

/* The following proposition, expressed in the `Context language` `English`, claims that the `Sign` `alhimar` means the `Referent` `donkey` in the `Domain` `Arabic`. 

In a separate proposition, expressed in the `Context language` `English`, the sign `الحمار` means the `Referent` `donkey` in the `Domain` `Arabic`. 

Transitively, the lemma `donkey` is known to mean `alhimar`, as well as `الحمار`*/

---

# Group Statements

All API endpoints are prepended by the ISO code of the context language. In this way the set of context languages is constrained to those with established ISO codes.

Some examples of top levels might be:

- `/eng`
- `/yid`

### References `[/{context_language}]`

##### Establish a relationship `[POST]`

The client can create new references in the system by posting to the context language endpoint. Each POST represents a single identity relationship, with a variable number of members. Every member is understood to be in the single relationship.

+ {domain} (string) - {sign}

For instance, posted to /eng:

+ Request (application/json)

    ```json
    {
       "english": "english",       
       "italian": "inglese",
       "german": "englisch",
    }
    ```

asserts three references about the same referent (in this case, the English language). The keys - the domain elements - are all signs in the context language and the values are asserted as signs in their domains.

+ Request (application/json)

    ```json
    {
        "english": "english",
        "russian": "английский"
    }
    ```

Would then assert an additional references about the same referent.

---

# Open questions

Currently the system doesn't admit homonyms<sup>[3](#footnote3)</sup> within a domain. It will probably be necessary to introduce a third, optional parameter to the domain/sign dyad to indicate context. My intuition tells me that these should be free strings, that don't need to be signs in any particular domain (that is, that don't need themselves to have referents), and only need to be unique as tags within domains.

---
###Definitions

<a name="footnote1">1.</a> A [lemma](https://en.wikipedia.org/wiki/Lemma_(morphology)) (plural *lemmas*) is the canonical form, dictionary form, or citation form of a set of words. In English, for example, run, runs, ran and running are forms of the same [lexeme](https://en.wikipedia.org/wiki/Lexeme), with *run* as the lemma.

<a name="footnote2">2.</a> A Content Object is a package of meaning or information. Within Poly, it is a word or phrase. This may be a string of text in any writing system, as well as media in image, audio and video formats. 

<a name="footnote3">3.</a> A homonym is defined as each of two or more words having the same spelling but different meanings and origins (e.g., pole of a tent and North Pole); also called a homograph.]
