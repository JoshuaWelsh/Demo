# demo
Sample Projects for Future Collaborators

COLLATZ GENERATOR

  Purpose:
    The Collatz Generator [DEPRECATED] programs are recoded from an early math project. They function as a low complexity RNG 
    stream, using the branching of the Collatz Conjecture to denote 1s or 0s in a binary stream which is converted to a decimal
    value.
  
  Deprecation Statement:
    The project has been deprecated, because the results do not display sufficient variance on the entire domain of 32 bit integers.
  
  Continued Use:
    The seed method is independently useful, and provides a method of ensuring system, instance, and time dependence of seeds.
     
    The generator may still be useful for providing seemingly random inputs in test enviroments. It is recommended that the range be
    restricted in the same manner as Java's native RNG, by using the modular operator.

  Version History:
    V1.0 Supports positive integers and streams of approximately 2 billion random integers.
    V1.1 Supports all integers, and infinite streams.

WEIGHTED SUM
  
  Purpose:
    The Weighted Sum program is sample code (with unit tests) from a 2019 programming competition, for which I won a prize.
    Competition Page: https://www.seminolestate.edu/computers/competition/results
  
  Version History:
    This program was recoded, with unit tests, after the time based competition.
