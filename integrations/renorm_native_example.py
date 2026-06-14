"""
Renorm-Native Integration Example
---------------------------------

This module demonstrates how to use the fused CUDA kernel provided by
`renorm-native` inside the Sentinel-Cardio architecture.

The fused operator performs:
    • normalization
    • ε-stabilized renormalization
    • linear projection
in a single GPU pass.

This reduces memory bandwidth pressure and improves numerical stability
for long-sequence, high-integrity workloads.
"""

import torch
from renorm.layers import FusedRenormLinearFunction


def renorm_fused_demo(
    batch_size: int = 32,
    sequence_length: int = 2048,
    hidden_dim: int = 128,
    epsilon: float = 0.05,
    device: str = None,
):
    """
    Runs a forward pass through the fused Renorm-Native kernel.

    Args:
        batch_size: Number of samples in the batch.
        sequence_length: Length of the sequence dimension.
        hidden_dim: Feature dimension for normalization + linear projection.
        epsilon: Stability constant for renormalization.
        device: "cuda" or "cpu". Defaults to CUDA if available.

    Returns:
        Tensor: Stabilized output from the fused kernel.
    """

    device = torch.device(device or ("cuda" if torch.cuda.is_available() else "cpu"))

    # Input tensor
    x = torch.randn(batch_size, sequence_length, hidden_dim, device=device)

    # Weight + bias for the fused linear projection
    w = torch.randn(hidden_dim, hidden_dim, device=device)
    b = torch.randn(hidden_dim, device=device)

    # Fused forward pass
    out = FusedRenormLinearFunction.apply(x, w, b, epsilon)

    return out


if __name__ == "__main__":
    y = renorm_fused_demo()
    print("Output shape:", y.shape)
