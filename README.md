# String Similarity Algorithms

Common string similarity algorithms `sim: (Σ* × Σ*) → [0, 1]`.

> Open value range algorithms (like Hamming) are normalized.

## Hamming 

**Complexity:** `O(n)`

``` python
def hamming_distance(str1: str, str2: str) -> int
```

``` python
def hamming(str1: str, str2: str) -> float
```

> The shorter string is padded with blank symbols to apply the algorithm.

## Levenshtein

**Complexity:** `O(n²)`

``` python
def levenshtein_distance(str1: str, str2: str) -> int
```

``` python
def levenshtein(str1: str, str2: str) -> float
```

## Damerau-Levenshtein

**Complexity:** `O(n²)`

``` python
def damerau_levenshtein_distance(str1: str, str2: str) -> int
```

``` python
def damerau_levenshtein(str1: str, str2: str) -> float
```

## Jaro

**Complexity:** `O(n²)`

``` python
def jaro(str1: str, str2: str) -> float
```

## Jaro-Winkler

**Complexity:** `O(n²)`

``` python
def jaro_winkler(str1: str, str2: str, p: float = 0.1) -> float
```

## Jaccard

**Complexity:** `O(n)`

``` python
def jaccard(str1: str, str2: str) -> float
```

> The set based similarity algorithms use character and index combination to mimic set element identity (`{ (character, index) ∀ c ∈ S₁, S₂ }`).

## Sørensen-Dice

**Complexity:** `O(n)`

``` python
def sorensen_dice(str1: str, str2: str) -> float
```

## Szymkiewicz-Simpson

**Complexity:** `O(n)`

``` python
def szymkiewicz_simpson(str1: str, str2: str) -> float
```

> Szymkiewicz-Simpson is also simply known as “overlap”.
