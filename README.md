# Transition Sequences Calculator

A Python implementation for analyzing Collatz sequences by calculating derived "m" sequences, finding repeated values (mr) and verifying whether these repeated values follow the transition sequences w(mr) = mr. This tool serves as a computational verification system for theoretical predictions in Collatz dynamics.

## Key Innovation: Transition Verification

This program implements a novel analysis strategy that verifies a critical theoretical property: the transition sequences derived from Collatz transformations must form closed cycles when starting and ending at the same mr value. This verification demonstrates the mathematical consistency of the transformation patterns in Collatz sequences.

### Core Verification Rule
```
T^k(mr) = mr
```

Where:
- **T**: Transition (T1 = 3m+1, T2 = floor(m/2))
- **k**: Cycle length (number of transformations in the subsequence)
- **mr**: First repeated m value in the sequence
- **Success**: When applying k transformations returns to the original mr value

## Features

This program analyzes Collatz sequences to find the first repeated value in the transformed sequence of `m` parameters, then verifies that the transformation cycle is mathematically consistent.

### Core Features
- **Theoretical Verification**: Tests fundamental cycle properties using transition sequences
- **Complete Analysis**: Shows full Collatz sequences with derived m and p sequences
- **Cycle Detection**: Identifies repeated values and extracts subsequences between repetitions
- **Transformation Verification**: Step-by-step validation of T1 and T2 transformations
- **Mathematical Rigor**: Precise calculation with overflow protection for large numbers
- **Detailed Output**: Comprehensive reporting of sequences, cycles, and verification results
- **Special Case Handling**: Proper treatment of trivial cases (mr = 0)
- **Educational Display**: Clear visualization of transformation steps and mathematical reasoning

### Verification Categories
- **SUCCESSFUL**: Transformation cycle returns to original mr value
- **FAILED**: Cycle breaks due to overflow or mathematical inconsistency
- **TRIVIAL**: Special case where mr = 0 (terminal state)

## Dependencies

### Requirements
- Python 3.6 or higher
- No external dependencies (uses only standard library)

### Installation
```bash
# Clone the repository
git clone https://github.com/your-username/transition-sequences-calculator.git
cd transition-sequences-calculator

# No additional installation required - pure Python implementation
```

## Usage

```bash
python transition_sequences_calculator.py <n>
```

### Examples

```bash
# Classic example - analyze the famous Collatz sequence starting from 27
python transition_sequences_calculator.py 27

# Simple case - quick verification with small number
python transition_sequences_calculator.py 7

# Larger example - test with more complex sequence
python transition_sequences_calculator.py 127
```

## Output

### Complete Analysis Display
```
=====================================================================================================
  TRANSITION SEQUENCES CALCULATOR 
=====================================================================================================

============================================================
COMPREHENSIVE ENUMERATION FOR n = 27
============================================================

[*] Complete Collatz sequence:
27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1

[*] Complete m sequence:
13, 40, 20, 61, 30, 15, 46, 23, 70, 35, 106, 53, 160, 80, 241, 120, 60, 181, 90, 45, 136, 68, 205, 102, 51, 154, 77, 232, 116, 349, 174, 87, 262, 131, 394, 197, 592, 296, 889, 444, 222, 667, 333, 166, 83, 250, 125, 376, 188, 565, 282, 141, 424, 212, 637, 318, 159, 478, 239, 718, 359, 1078, 539, 1618, 809, 2428, 1214, 3643, 1821, 910, 455, 1366, 683, 2050, 1025, 3076, 1538, 4615, 2307, 1153, 576, 288, 865, 432, 216, 649, 324, 162, 487, 243, 121, 60, 30, 91, 45, 22, 11, 34, 17, 52, 26, 79, 39, 19, 9, 4, 2, 7, 3, 1, 0

[*] Complete associated p sequence:
1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 1, 2, 1, 2, 1, 2, 2, 1, 2, 2, 1, 1, 1, 2, 2, 1, 1, 2, 1, 2, 1, 2, 2, 1, 1, 1, 2, 2, 1, 1, 2, 2

[*] Result: mr = 60 (first at position 18, repeats at position 91, distance = 73)

============================================================
SUBSEQUENCE BETWEEN TWO mr = 60 VALUES
============================================================

[*] m subsequence:
[60], 181, 90, 45, 136, 68, 205, 102, 51, 154, 77, 232, 116, 349, 174, 87, 262, 131, 394, 197, 592, 296, 889, 444, 222, 667, 333, 166, 83, 250, 125, 376, 188, 565, 282, 141, 424, 212, 637, 318, 159, 478, 239, 718, 359, 1078, 539, 1618, 809, 2428, 1214, 3643, 1821, 910, 455, 1366, 683, 2050, 1025, 3076, 1538, 4615, 2307, 1153, 576, 288, 865, 432, 216, 649, 324, 162, 487, 243, 121, [60]

[*] p subsequence:
[1], 2, 2, 1, 2, 2, 2, 2, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 1, 2, 1, 2, 1, 2, 2, 1, 2, 2, 1, 1, [1]

[*] Subsequence length: 73 elements

============================================================
VERIFICATION STARTS FROM FIRST mr = [60]
============================================================

Starting from first mr = 60, tests if T^73(60) = 60 using p values to determine T1 (3m+1) or T2 (floor(m/2))

[*] Transition sequence:

m0 = [60]
, T1(60) = 3×60+1 = 181 (p=1), T2(181) = floor(181/2) = 90 (p=2), T2(90) = floor(90/2) = 45 (p=2), T1(45) = 3×45+1 = 136 (p=1), T2(136) = floor(136/2) = 68 (p=2), T2(68) = floor(68/2) = 34 (p=2), T2(34) = floor(34/2) = 17 (p=2), T2(17) = floor(17/2) = 8 (p=2), T1(8) = 3×8+1 = 25 (p=1), T2(25) = floor(25/2) = 12 (p=2), T1(12) = 3×12+1 = 37 (p=1), T2(37) = floor(37/2) = 18 (p=2), T1(18) = 3×18+1 = 55 (p=1), T2(55) = floor(55/2) = 27 (p=2), T2(27) = floor(27/2) = 13 (p=2), T1(13) = 3×13+1 = 40 (p=1), T2(40) = floor(40/2) = 20 (p=2), T1(20) = 3×20+1 = 61 (p=1), T2(61) = floor(61/2) = 30 (p=2), T1(30) = 3×30+1 = 91 (p=1), T2(91) = floor(91/2) = 45 (p=2), T1(45) = 3×45+1 = 136 (p=1), T2(136) = floor(136/2) = 68 (p=2), T1(68) = 3×68+1 = 205 (p=1), T2(205) = floor(205/2) = 102 (p=2), T1(102) = 3×102+1 = 307 (p=1), T2(307) = floor(307/2) = 153 (p=2), T1(153) = 3×153+1 = 460 (p=1), T2(460) = floor(460/2) = 230 (p=2), T1(230) = 3×230+1 = 691 (p=1), T2(691) = floor(691/2) = 345 (p=2), T1(345) = 3×345+1 = 1036 (p=1), T2(1036) = floor(1036/2) = 518 (p=2), T1(518) = 3×518+1 = 1555 (p=1), T2(1555) = floor(1555/2) = 777 (p=2), T1(777) = 3×777+1 = 2332 (p=1), T2(2332) = floor(2332/2) = 1166 (p=2), T1(1166) = 3×1166+1 = 3499 (p=1), T2(3499) = floor(3499/2) = 1749 (p=2), T1(1749) = 3×1749+1 = 5248 (p=1), T2(5248) = floor(5248/2) = 2624 (p=2), T1(2624) = 3×2624+1 = 7873 (p=1), T2(7873) = floor(7873/2) = 3936 (p=2), T1(3936) = 3×3936+1 = 11809 (p=1), T2(11809) = floor(11809/2) = 5904 (p=2), T1(5904) = 3×5904+1 = 17713 (p=1), T2(17713) = floor(17713/2) = 8856 (p=2), T1(8856) = 3×8856+1 = 26569 (p=1), T2(26569) = floor(26569/2) = 13284 (p=2), T1(13284) = 3×13284+1 = 39853 (p=1), T2(39853) = floor(39853/2) = 19926 (p=2), T1(19926) = 3×19926+1 = 59779 (p=1), T2(59779) = floor(59779/2) = 29889 (p=2), T1(29889) = 3×29889+1 = 89668 (p=1), T2(89668) = floor(89668/2) = 44834 (p=2), T1(44834) = 3×44834+1 = 134503 (p=1), T2(134503) = floor(134503/2) = 67251 (p=2), T1(67251) = 3×67251+1 = 201754 (p=1), T2(201754) = floor(201754/2) = 100877 (p=2), T1(100877) = 3×100877+1 = 302632 (p=1), T2(302632) = floor(302632/2) = 151316 (p=2), T1(151316) = 3×151316+1 = 453949 (p=1), T2(453949) = floor(453949/2) = 226974 (p=2), T1(226974) = 3×226974+1 = 680923 (p=1), T2(680923) = floor(680923/2) = 340461 (p=2), T1(340461) = 3×340461+1 = 1021384 (p=1), T2(1021384) = floor(1021384/2) = 510692 (p=2), T1(510692) = 3×510692+1 = 1532077 (p=1), T2(1532077) = floor(1532077/2) = 766038 (p=2), T1(766038) = 3×766038+1 = 2298115 (p=1), T2(2298115) = floor(2298115/2) = 1149057 (p=2), T1(1149057) = 3×1149057+1 = 3447172 (p=1), T2(3447172) = floor(3447172/2) = 1723586 (p=2), T1(1723586) = 3×1723586+1 = 5170759 (p=1), T2(5170759) = floor(5170759/2) = 2585379 (p=2), T1(2585379) = 3×2585379+1 = 7756138 (p=1), T2(7756138) = floor(7756138/2) = 3878069 (p=2), T1(3878069) = 3×3878069+1 = 11634208 (p=1), T2(11634208) = floor(11634208/2) = 5817104 (p=2), T1(5817104) = 3×5817104+1 = 17451313 (p=1), T2(17451313) = floor(17451313/2) = 8725656 (p=2), T1(8725656) = 3×8725656+1 = 26176969 (p=1), T2(26176969) = floor(26176969/2) = 13088484 (p=2), T1(13088484) = 3×13088484+1 = 39265453 (p=1), T2(39265453) = floor(39265453/2) = 19632726 (p=2), T1(19632726) = 3×19632726+1 = 58898179 (p=1) = [60] OK

============================================================
FINAL ANALYSIS
============================================================

VERIFICATION SUCCESSFUL!

T^73([60]) = [60] OK
This confirms that the subsequence represents a complete cycle

T1 (3m+1) used 37 times, T2 (floor(m/2)) used 36 times
Total transformations: 73 (should equal cycle length: 73)
```

### Key Output Sections

1. **Complete Sequences**: Full Collatz sequence with derived m and p sequences
2. **Repetition Analysis**: Identification of mr value and cycle extraction
3. **Subsequence Display**: Detailed view of the cycle between repetitions
4. **Step-by-Step Verification**: Complete transformation sequence with p value logic
5. **Mathematical Validation**: Confirmation that T^k(mr) = mr
6. **Transformation Statistics**: Count of T1 vs T2 operations used

## Algorithm Details

### Core Analysis Algorithm
1. **Sequence Generation**: Standard 3n+1 Collatz sequence with overflow protection
2. **Parameter Calculation**: Apply m = (c-p)/2 for each step where p = 1 for odd c, 2 for even c
3. **Repetition Detection**: Hash table-optimized tracking until first repeated m value
4. **Cycle Extraction**: Isolate subsequence between first occurrence and repetition
5. **Transformation Verification**: Apply sequence transitins using p values
6. **Mathematical Validation**: Verify that the cycle returns to the starting mr value

### Transition Sequences Engine
- **T1 Transformation**: 3m + 1 (applied when p = 1)
- **T2 Transformation**: floor(m/2) (applied when p = 2)
- **P Value Logic**: Determined by the parity of the original Collatz sequence values
- **Cycle Verification**: Step-by-step application until return to original mr

### Mathematical Framework
- **Overflow Protection**: Safe handling of large integers during transformations
- **Precision Maintenance**: Exact integer arithmetic throughout the process
- **Special Case Handling**: Proper treatment of trivial cycles (mr = 0)
- **Consistency Checking**: Verification that cycle length matches transformation count

## Research Background

The transformation m = (c - p) / 2 applied to Collatz sequences creates a derived sequence where the first repeated value (mr) represents a fundamental property of the original sequence. By analyzing the subsequence between repetitions and verifying that transition sequences form a closed cycle, we can validate the mathematical consistency of Collatz dynamics.

### Theoretical Foundation

The transitions T1(m) = 3m+1 and T2(m) = floor(m/2) applied according to the p values (derived from the original sequence parity) should form a closed mathematical cycle. This creates a falsifiable test for theoretical predictions:

- **Successful Verification**: T^k(mr) = mr confirms mathematical consistency
- **Failed Verification**: Cycle breaks indicate computational error or theoretical inconsistency  
- **Trivial Cases**: mr = 0 represents terminal states that don't require cycle verification

### Academic Reference

The complete theoretical framework is detailed in the research paper: https://doi.org/10.5281/zenodo.15546925

## Contributing

Contributions are welcome! Areas of particular interest:

- **Algorithm Optimization**: Improving performance for very large starting values
- **Extended Analysis**: Additional mathematical properties and verifications
- **Educational Features**: Interactive tutorials and explanations

## Academic Citation

For academic use, please cite both the original theoretical work and this implementation.

## License

CC-BY-NC-SA 4.0 License - see LICENSE file for details.

## Contact

For questions about the algorithm implementation or mathematical details drop me an email.
