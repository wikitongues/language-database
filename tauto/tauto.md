FORMAT: .1

# WID - Lemma[^1] reference engine

We are defining an API to be used for associating and retrieving associations between/among given words in a language-agnostic context. The first use of this service will be the population and retrieval of language names.

The API will expose a single resource: A reference. A reference has 4 components:

- Sign
- Domain
- * Referent 
- Context/Host language

Roughly speaking, these express the statement, "[Sign] means [Referent] in [Domain]", where the context language is the language of the statement itself. The referent is an integral part of a reference statement but will remain internal to the system.

The system can be expressed as a series of propositions of this form.

## Sign

A sign is a *content object*[^1] which is the realization of a *referent* within a given *domain*. In the context of human language, it is a language vocabulary element.

## Domain

A domain is also a *content object*, representing the domain within s associated sign is valid. In the context of human language, it is the name of the language that possesses a vocabulary element. Because a) the set of languages is not fixed, or known; and b) the system cannot privilege any particular linguistic expression of any entity, the domain element is as dynamic and provisional as the sign element. 

## Referent

Every entity or "object" in the system will be represented by a single referent. Multiple statements with the same referent will be understood to have a *translational* relationship; that is, to be realizations of the same referent in their respective domains. However, the referent is a bare identifier without any semantics of its own, and doesn't privilege any given expression. Therefore any reference to a referent entity will necessarily be through one of its representations; the client cannot invoke an object directly.

The initial population will be the known human languages.

## Host language

The interface or context language of the pairing. Every interaction with the system necessarily will be in a given linguistic context; for instance, this might most commonly be the interface language of the application being used. It might be productively assumed to be the native language of the user of the system. Host languages can act as namespaces for statements, but necessarily so; if a context language contains a statement about a given domain, that statement will be 'in scope' within that context; however, the statement may also be in scope in other contexts without specifically expressed statements.

To give a concrete example: if a non-Latin context language like Arabic contains a statement about the English word "donkey" (rendered, presumably, in Arabic script), that statement will be accessible in any query on English from within the context. But a statement about the English word "donkey" in the English context, rendered normally, will in all likelihood be available in other Latin-alphabet contexts, without it needing to be repeatedly established that the English word is "donkey".

[^1]: The first and most obvious content object is *string*, however we will proceed with the understanding that image, audio and video content might be the most appropriate format for content in a given context.

# Group Statements

All API endpoints are prepended by the ISO code of the context language. In this way the set of context languages is constrained to those with established ISO codes.

Some examples of top levels might be:

- /eng
- /yid

## References [/{context_language}]

### Establish a relationship [POST]

The client can create new references in the system by posting to the context language endpoint. Each POST represents a single identity relationship, with a variable number of members. Every member is understood to be in the single relationship.

+ {domain} (string) - {sign}

For instance, posted to /eng:

+ Request (application/json)

    {
       "english": "english",
       "italian": "inglese",
       "german": "englisch",
    }

Asserts three references about the same referent (in this case, the English language). The keys - the domain elements - are all signs in the context language and the values are asserted as signs in their domains.

+ Request (application/json)

    {
        "english": "english",
        "russian": "английский"
    }

Would then assert an additional references about the same referent.

# Open questions

Currently the system doesn't admit homonyms within a domain. It will probably be necessary to introduce a third, optional parameter to the domain/sign dyad to indicate context. My intuition tells me that these should be free strings, that don't need to be signs in any particular domain (that is, that don't need themselves to have referents), and only need to be unique as tags within domains.
