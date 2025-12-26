"""
Physics Lesson: Stable and Unstable Equilibrium
================================================

This script demonstrates the concepts of stable and unstable equilibrium
using potential energy functions and force analysis.

Key Concepts:
- Equilibrium occurs where force F = -dU/dx = 0
- Stable equilibrium: U has a local minimum (d²U/dx² > 0)
- Unstable equilibrium: U has a local maximum (d²U/dx² < 0)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve


def potential_energy(x):
    """
    Define a potential energy function with multiple equilibrium points.
    U(x) = x^4 - 4x^2 + x
    
    This function has:
    - Local minima (stable equilibria)
    - Local maxima (unstable equilibria)
    """
    return x**4 - 4*x**2 + x


def force(x):
    """
    Force is the negative derivative of potential energy.
    F(x) = -dU/dx = -4x^3 + 8x - 1
    """
    return -4*x**3 + 8*x - 1


def second_derivative(x):
    """
    Second derivative of potential energy.
    d²U/dx² = 12x^2 - 8
    
    Positive: stable equilibrium (local minimum)
    Negative: unstable equilibrium (local maximum)
    """
    return 12*x**2 - 8


def find_equilibrium_points():
    """Find points where force = 0 (equilibrium positions)"""
    # Find roots of the force equation
    equilibrium_points = []
    
    # Search for equilibrium points in different regions
    for x_guess in [-2, 0, 2]:
        try:
            x_eq = fsolve(force, x_guess)[0]
            # Check if this is a new equilibrium point
            is_new = all(abs(x_eq - x_existing) > 0.1 for x_existing in equilibrium_points)
            if is_new and abs(force(x_eq)) < 1e-6:
                equilibrium_points.append(x_eq)
        except:
            pass
    
    return sorted(equilibrium_points)


def classify_equilibrium(x_eq):
    """
    Classify equilibrium point as stable or unstable.
    Returns: 'stable' if d²U/dx² > 0, 'unstable' if d²U/dx² < 0
    """
    d2U = second_derivative(x_eq)
    if d2U > 0:
        return 'stable', d2U
    elif d2U < 0:
        return 'unstable', d2U
    else:
        return 'neutral', d2U


def create_visualization():
    """Create comprehensive visualization of equilibrium concepts"""
    # Create x values for plotting
    x = np.linspace(-2.5, 2.5, 1000)
    U = potential_energy(x)
    F = force(x)
    
    # Find equilibrium points
    eq_points = find_equilibrium_points()
    
    # Create figure with subplots
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 10))
    fig.suptitle('Physics Lesson: Stable and Unstable Equilibrium', 
                 fontsize=16, fontweight='bold')
    
    # Plot 1: Potential Energy Function
    ax1.plot(x, U, 'b-', linewidth=2, label='Potential Energy U(x)')
    ax1.axhline(y=0, color='k', linestyle='--', alpha=0.3)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlabel('Position x', fontsize=12)
    ax1.set_ylabel('Potential Energy U(x)', fontsize=12)
    ax1.set_title('Potential Energy Function: U(x) = x⁴ - 4x² + x', fontsize=13)
    
    # Mark equilibrium points on potential energy curve
    for x_eq in eq_points:
        stability, d2U = classify_equilibrium(x_eq)
        color = 'green' if stability == 'stable' else 'red'
        marker = 'v' if stability == 'stable' else '^'
        label = f'{stability.capitalize()}: x={x_eq:.2f}'
        ax1.plot(x_eq, potential_energy(x_eq), marker, 
                color=color, markersize=15, label=label)
    
    ax1.legend(fontsize=10)
    
    # Plot 2: Force Function
    ax2.plot(x, F, 'r-', linewidth=2, label='Force F(x) = -dU/dx')
    ax2.axhline(y=0, color='k', linestyle='--', alpha=0.5, linewidth=1.5)
    ax2.grid(True, alpha=0.3)
    ax2.set_xlabel('Position x', fontsize=12)
    ax2.set_ylabel('Force F(x)', fontsize=12)
    ax2.set_title('Force (Negative Gradient of Potential)', fontsize=13)
    
    # Mark equilibrium points on force curve
    for x_eq in eq_points:
        stability, d2U = classify_equilibrium(x_eq)
        color = 'green' if stability == 'stable' else 'red'
        ax2.plot(x_eq, 0, 'o', color=color, markersize=12)
        ax2.annotate(f'x={x_eq:.2f}', 
                    xy=(x_eq, 0), 
                    xytext=(x_eq, 0.5),
                    fontsize=9,
                    ha='center',
                    arrowprops=dict(arrowstyle='->', color=color, lw=1.5))
    
    ax2.legend(fontsize=10)
    
    # Plot 3: Physical Interpretation with Ball Analogy
    ax3.plot(x, U, 'b-', linewidth=3, alpha=0.6)
    ax3.fill_between(x, U, -6, alpha=0.1, color='blue')
    ax3.set_xlabel('Position x', fontsize=12)
    ax3.set_ylabel('Potential Energy U(x)', fontsize=12)
    ax3.set_title('Physical Interpretation: Ball on Energy Surface', fontsize=13)
    ax3.grid(True, alpha=0.3)
    ax3.set_ylim(-6, 3)
    
    # Add ball representations at equilibrium points
    for x_eq in eq_points:
        stability, d2U = classify_equilibrium(x_eq)
        U_eq = potential_energy(x_eq)
        
        if stability == 'stable':
            # Ball in valley (stable)
            circle = plt.Circle((x_eq, U_eq - 0.3), 0.15, 
                              color='green', alpha=0.8, zorder=5)
            ax3.add_patch(circle)
            ax3.annotate('STABLE\n(returns to equilibrium)', 
                        xy=(x_eq, U_eq - 0.3), 
                        xytext=(x_eq, U_eq - 2),
                        fontsize=9,
                        ha='center',
                        bbox=dict(boxstyle='round,pad=0.5', facecolor='lightgreen', alpha=0.7),
                        arrowprops=dict(arrowstyle='->', color='green', lw=2))
        else:
            # Ball on peak (unstable)
            circle = plt.Circle((x_eq, U_eq + 0.3), 0.15, 
                              color='red', alpha=0.8, zorder=5)
            ax3.add_patch(circle)
            ax3.annotate('UNSTABLE\n(moves away)', 
                        xy=(x_eq, U_eq + 0.3), 
                        xytext=(x_eq, U_eq + 1.5),
                        fontsize=9,
                        ha='center',
                        bbox=dict(boxstyle='round,pad=0.5', facecolor='lightcoral', alpha=0.7),
                        arrowprops=dict(arrowstyle='->', color='red', lw=2))
    
    plt.tight_layout()
    
    return fig, eq_points


def print_analysis(eq_points):
    """Print detailed analysis of equilibrium points"""
    print("\n" + "="*70)
    print("EQUILIBRIUM ANALYSIS")
    print("="*70)
    print("\nPotential Energy Function: U(x) = x⁴ - 4x² + x")
    print("Force: F(x) = -dU/dx = -4x³ + 8x - 1")
    print("\n" + "-"*70)
    print(f"{'Position':<15} {'U(x)':<15} {'Stability':<15} {'d²U/dx²':<15}")
    print("-"*70)
    
    for x_eq in eq_points:
        U_eq = potential_energy(x_eq)
        stability, d2U = classify_equilibrium(x_eq)
        print(f"{x_eq:<15.4f} {U_eq:<15.4f} {stability.upper():<15} {d2U:<15.4f}")
    
    print("-"*70)
    print("\nPhysical Interpretation:")
    print("• STABLE equilibrium (d²U/dx² > 0):")
    print("  - Potential energy is at a local minimum")
    print("  - Small displacements result in restoring forces")
    print("  - System returns to equilibrium (like a ball in a valley)")
    print("\n• UNSTABLE equilibrium (d²U/dx² < 0):")
    print("  - Potential energy is at a local maximum")
    print("  - Small displacements result in forces pushing away")
    print("  - System moves away from equilibrium (like a ball on a hilltop)")
    print("="*70 + "\n")


def main():
    """Main function to run the equilibrium lesson"""
    print("\n" + "="*70)
    print("PHYSICS LESSON: STABLE AND UNSTABLE EQUILIBRIUM")
    print("="*70)
    
    # Find and analyze equilibrium points
    eq_points = find_equilibrium_points()
    
    # Print analysis
    print_analysis(eq_points)
    
    # Create visualization
    fig, eq_points = create_visualization()
    
    # Save the figure
    output_file = 'equilibrium_lesson_output.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Visualization saved as: {output_file}")
    
    # Display the plot
    plt.show()
    
    print("\nLesson complete! The visualization shows:")
    print("1. Top panel: Potential energy curve with equilibrium points marked")
    print("2. Middle panel: Force curve showing where F=0 (equilibrium)")
    print("3. Bottom panel: Physical interpretation with ball analogy")


if __name__ == "__main__":
    main()
