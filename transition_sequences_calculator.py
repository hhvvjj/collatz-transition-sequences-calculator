#########################################################################################################
# transition_sequences_calculator.py
#
# Implementation to analyze Collatz sequences by calculating derived "m" sequences,
# finding repeated values (mr) and  verifying whether these repeated values follow 
# the transition sequences w(mr) = mr.
#
# The complete article can be found on https://doi.org/10.5281/zenodo.15546925
#
#########################################################################################################


#!/usr/bin/env python3


import sys
from typing import List, Tuple, Optional
from dataclasses import dataclass

# Constants
MAX_SEQUENCE_LENGTH = 10000
MAX_TRANSFORMATION_LENGTH = 100
MAX_SAFE_VALUE = 2**64 - 1


@dataclass
class SequenceData:
    """Container for sequence analysis data"""
    collatz_seq: List[int]
    m_seq: List[int]
    p_seq: List[int]
    mr_value: int
    mr_first_pos: int
    mr_repeat_pos: int
    cycle_length: int


class CollatzAnalyzer:
    """Main analyzer for Collatz sequences and MR transformations"""
    
    def __init__(self, n: int):
        if n < 1:
            raise ValueError(f"n must be >= 1, got {n}")
        self.n = n
        self.seen_m_values = set()
    
    @staticmethod
    def calculate_m(c: int) -> int:
        """Calculate parameter m for a Collatz value: m = (c-p)/2"""
        p = 2 if c % 2 == 0 else 1
        return (c - p) // 2
    
    @staticmethod
    def apply_transition(m: int, p: int) -> int:
        """Apply transitions based on p value: T1(m) = 3m+1, T2(m) = floor(m/2)"""
        return 3 * m + 1 if p == 1 else m // 2
    
    @staticmethod
    def collatz_step(n: int) -> int:
        """Apply single Collatz transformation step"""
        return n // 2 if n % 2 == 0 else 3 * n + 1
    
    @staticmethod
    def calculate_p(c: int) -> int:
        """Calculate parameter p for a Collatz value"""
        return 2 if c % 2 == 0 else 1
    
    def _generate_collatz_sequence(self) -> Tuple[List[int], List[int], List[int]]:
        """Generate Collatz, m and p sequences"""
        collatz_seq = [self.n]
        m_seq = []
        p_seq = []
        
        n = self.n
        while len(collatz_seq) < MAX_SEQUENCE_LENGTH and n != 1:
            m = self.calculate_m(n)
            p = self.calculate_p(n)
            
            m_seq.append(m)
            p_seq.append(p)
            
            # Apply Collatz transformation
            if n > MAX_SAFE_VALUE // 3 and n % 2 == 1:
                break
            n = self.collatz_step(n)
            collatz_seq.append(n)
        
        # Handle final n=1 case
        if n == 1:
            m_seq.append(self.calculate_m(n))
            p_seq.append(self.calculate_p(n))
        
        return collatz_seq, m_seq, p_seq
    
    def _find_mr_repetition(self, m_seq: List[int]) -> Tuple[Optional[int], int, int]:
        """Find first repeated m value and its positions"""
        seen = {}
        
        for i, m in enumerate(m_seq):
            if m in seen:
                return m, seen[m], i
            seen[m] = i
        
        # No repetition found, check for trivial case
        if m_seq and m_seq[-1] == 0:
            return 0, len(m_seq) - 1, len(m_seq) - 1
        
        return None, -1, -1
    
    def analyze_sequence(self) -> Optional[SequenceData]:
        """Perform complete sequence analysis"""
        collatz_seq, m_seq, p_seq = self._generate_collatz_sequence()
        
        if not m_seq:
            return None
        
        mr_value, mr_first_pos, mr_repeat_pos = self._find_mr_repetition(m_seq)
        
        if mr_value is None:
            return None
        
        cycle_length = mr_repeat_pos - mr_first_pos if mr_value != 0 else 0
        
        return SequenceData(
            collatz_seq=collatz_seq,
            m_seq=m_seq,
            p_seq=p_seq,
            mr_value=mr_value,
            mr_first_pos=mr_first_pos,
            mr_repeat_pos=mr_repeat_pos,
            cycle_length=cycle_length
        )


class OutputFormatter:
    """Handles all output formatting and display"""
    
    @staticmethod
    def print_sequence(name: str, seq: List[int], highlight_positions: Optional[List[int]] = None) -> None:
        """Print a sequence with optional highlighting"""
        print(f"{name}", end="")
        highlight_positions = highlight_positions or []
        
        for i, value in enumerate(seq):
            if i > 0:
                print(", ", end="")
            
            if i in highlight_positions:
                print(f"[{value}]", end="")
            else:
                print(f"{value}", end="")
        print()
       
    @staticmethod
    def print_analysis_header(n: int) -> None:
        """Print analysis header"""
        print("")
        print("=" * 95)
        print("  TRANSITION SEQUENCES CALCULATOR ")
        print("=" * 95)
        print("")
        print(f"{'='*60}")
        print(f"COMPREHENSIVE ENUMERATION FOR n = {n}")
        print(f"{'='*60}")
        print("")

    @staticmethod
    def print_collatz_sequence(seq: List[int]) -> None:
        """Print Collatz sequence in a single line"""
        print("[*] Complete Collatz sequence:")
        print(", ".join(map(str, seq)))
    
    @staticmethod
    def print_subsequence_info(data: SequenceData) -> None:
        """Print extracted subsequence information"""
        if data.mr_value == 0:
            print(" -> mr = 0 (trivial cycle)")
            return
        
        print(f"\n[*] Result: mr = {data.mr_value} (first at position {data.mr_first_pos}, "
              f"repeats at position {data.mr_repeat_pos}, distance = {data.cycle_length})")
        
        print(f"\n{'='*60}")
        print(f"SUBSEQUENCE BETWEEN TWO mr = {data.mr_value} VALUES")
        print(f"{'='*60}")
        
        # Extract subsequence
        start, end = data.mr_first_pos, data.mr_repeat_pos + 1
        highlight_pos = [0, data.cycle_length]  # First and last positions
        
        print()
        OutputFormatter.print_sequence(
            "[*] m subsequence:\n", data.m_seq[start:end], highlight_pos
        )
        print()
        OutputFormatter.print_sequence(
            "[*] p subsequence:\n", data.p_seq[start:end], highlight_pos
        )
        print()
        print(f"[*] Subsequence length: {data.cycle_length} elements")


class TransitionVerifier:
    """Handles transition verification"""
    
    @staticmethod
    def _get_transformation_counts(p_values: List[int]) -> Tuple[int, int]:
        """Count T1 and T2 transformations"""
        t1_count = sum(1 for p in p_values if p == 1)
        t2_count = sum(1 for p in p_values if p == 2)
        return t1_count, t2_count
    
    @staticmethod
    def _print_transformation_step(current: int, p_val: int, next_val: int, is_last: bool, mr_value: int) -> None:
        """Print a single transformation step"""
        if p_val == 1:
            print(f", T1({current}) = 3×{current}+1 = {next_val} (p={p_val})", end="")
        else:
            print(f", T2({current}) = floor({current}/2) = {next_val} (p={p_val})", end="")
        
        if is_last:
            symbol = "OK" if next_val == mr_value else "ERROR"
            print(f" = [{next_val}] {symbol}", end="")
    
    @staticmethod
    def _print_verification_summary(success: bool, data: SequenceData, t1_count: int, t2_count: int) -> None:
        """Print verification summary and transformation counts"""
        print(f"\n\n{'='*60}")
        print("FINAL ANALYSIS")
        print(f"{'='*60}")
        print(f"\n{'VERIFICATION SUCCESSFUL' if success else 'VERIFICATION FAILED'}!")
        print()
        if success:
            print(f"T^{data.cycle_length}([{data.mr_value}]) = [{data.mr_value}] OK")
            print("This confirms that the subsequence represents a complete cycle")
        
        # Transformation summary
        print()
        print(f"T1 (3m+1) used {t1_count} times, T2 (floor(m/2)) used {t2_count} times")
        print(f"Total transformations: {t1_count + t2_count} (should equal cycle length: {data.cycle_length})")
    
    @staticmethod
    def _print_trivial_case_result() -> None:
        """Print result for trivial case (mr = 0)"""
        print()
        print("mr = 0 is the special case within the 42 elements, so no cycle verification needed for the trivial case")
        print()
        print("[*] Transition sequence:")
        print()
        print("m0 = [0] (trivial cycle - no transformations needed)")
        print(f"\n{'='*60}")
        print("FINAL ANALYSIS")
        print(f"{'='*60}")
        print("\nVERIFICATION SUCCESSFUL!")
        print()
        print("T^0([0]) = [0] OK")
        print("The value mr = 0 represents the terminal state (trivial cycle)")
        print()
        print("T1 (3m+1) used 0 times, T2 (floor(m/2)) used 0 times")
        print("Total transformations: 0 (trivial case with cycle length: 0)")
    
    @classmethod
    def verify_cycle_with_p_values(cls, data: SequenceData) -> None:
        """Verify cycle using correct p values"""
        if data.mr_value == 0:
            cls._print_trivial_case_result()
            return

        print()
        print(f"Starting from first mr = {data.mr_value}, tests if T^{data.cycle_length}({data.mr_value}) = {data.mr_value} using p values to determine T1 (3m+1) or T2 (floor(m/2))")
        print()
        
        current = data.mr_value
        print("[*] Transition sequence:")
        print()
        print(f"m0 = [{current}]", end="")
        print()

        # Get p values for the cycle
        p_values = data.p_seq[data.mr_first_pos:data.mr_first_pos + data.cycle_length]
        
        for i, p_val in enumerate(p_values):
            if current > MAX_SAFE_VALUE // 3:
                print(f"\n\n[*] Transformation result: VERIFICATION FAILED (overflow at step {i})")
                return
            
            next_val = CollatzAnalyzer.apply_transition(current, p_val)
            is_last = i == len(p_values) - 1
            cls._print_transformation_step(current, p_val, next_val, is_last, data.mr_value)
            current = next_val
        
        success = current == data.mr_value
        t1_count, t2_count = cls._get_transformation_counts(p_values)
        cls._print_verification_summary(success, data, t1_count, t2_count)


def validate_input() -> int:
    """Validate command line input"""
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <n>")
        print(f"Example: {sys.argv[0]} 27")
        print("\nThis program:")
        print("1. Calculates the m sequence for the given n")
        print("2. Finds the first repeated value (mr)")
        print("3. Analyzes the transformation sequence w(mr)")
        print("4. Checks if w(mr) = mr or finds cycles")
        print("\nNote: n must be >= 1\n")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
    except ValueError:
        print(f"Error: Invalid number '{sys.argv[1]}'. Please enter a valid integer.")
        sys.exit(1)
    
    if n < 1:
        print(f"Error: n must be >= 1. You entered: {n}")
        sys.exit(1)
    
    return n


def main() -> int:
    """Main program entry point"""
    n = validate_input()
    
    try:
        # Initialize analyzer
        analyzer = CollatzAnalyzer(n)
        formatter = OutputFormatter()
        
        # Print header
        formatter.print_analysis_header(n)
        
        # Analyze sequence
        data = analyzer.analyze_sequence()
        
        if not data:
            print("No mr found (overflow or limit reached)")
            return 1
        
        # Display results
        formatter.print_collatz_sequence(data.collatz_seq)
        print()
        
        # Display m and p sequences with highlights
        highlight_positions = []
        if data.mr_value != 0:
            highlight_positions = [data.mr_first_pos, data.mr_repeat_pos]
        
        formatter.print_sequence("[*] Complete m sequence:\n", data.m_seq, highlight_positions)
        print()
        formatter.print_sequence("[*] Complete associated p sequence:\n", data.p_seq, highlight_positions)
        
        # Display subsequence info
        formatter.print_subsequence_info(data)
        
        # Always show verification section
        print(f"\n{'='*60}")
        print(f"VERIFICATION STARTS FROM FIRST mr = [{data.mr_value}]")
        print(f"{'='*60}")
        
        # Verify transition cycle
        TransitionVerifier.verify_cycle_with_p_values(data)
        
        return 0
        
    except Exception as e:
        print(f"Error during analysis: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())