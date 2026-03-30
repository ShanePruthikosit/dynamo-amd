# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""Multimodal utilities for Dynamo components."""
from dynamo.common.constants import EmbeddingTransferMode
from dynamo.common.multimodal.async_encoder_cache import AsyncEncoderCache

try:
    from dynamo.common.multimodal.embedding_transfer import (
        LocalEmbeddingReceiver,
        LocalEmbeddingSender,
        NixlReadEmbeddingReceiver,
        NixlReadEmbeddingSender,
        NixlWriteEmbeddingReceiver,
        NixlWriteEmbeddingSender,
        TransferRequest,
    )
    from dynamo.common.multimodal.image_loader import ImageLoader
    LocalEmbeddingReceiver = LocalEmbeddingReceiver
    LocalEmbeddingSender = LocalEmbeddingSender
    NixlReadEmbeddingReceiver = NixlReadEmbeddingReceiver
    NixlReadEmbeddingSender = NixlReadEmbeddingSender
    NixlWriteEmbeddingReceiver = NixlWriteEmbeddingReceiver
    NixlWriteEmbeddingSender = NixlWriteEmbeddingSender
    TransferRequest = TransferRequest
    ImageLoader = ImageLoader
    _nixl_available = True
except ImportError:
    LocalEmbeddingReceiver = None
    LocalEmbeddingSender = None
    NixlReadEmbeddingReceiver = None
    NixlReadEmbeddingSender = None
    NixlWriteEmbeddingReceiver = None
    NixlWriteEmbeddingSender = None
    TransferRequest = None
    ImageLoader = None
    _nixl_available = False

if _nixl_available:
    EMBEDDING_SENDER_FACTORIES = {
        EmbeddingTransferMode.LOCAL: LocalEmbeddingSender,
        EmbeddingTransferMode.NIXL_WRITE: NixlWriteEmbeddingSender,
        EmbeddingTransferMode.NIXL_READ: NixlReadEmbeddingSender,
    }
    EMBEDDING_RECEIVER_FACTORIES = {
        EmbeddingTransferMode.LOCAL: LocalEmbeddingReceiver,
        EmbeddingTransferMode.NIXL_WRITE: NixlWriteEmbeddingReceiver,
        EmbeddingTransferMode.NIXL_READ: lambda: NixlReadEmbeddingReceiver(max_items=0),
    }
else:
    EMBEDDING_SENDER_FACTORIES = {}
    EMBEDDING_RECEIVER_FACTORIES = {}

__all__ = [
    "AsyncEncoderCache",
    "EMBEDDING_RECEIVER_FACTORIES",
    "EMBEDDING_SENDER_FACTORIES",
    "ImageLoader",
    "NixlReadEmbeddingReceiver",
    "NixlReadEmbeddingSender",
    "NixlWriteEmbeddingSender",
    "NixlWriteEmbeddingReceiver",
    "TransferRequest",
    "LocalEmbeddingReceiver",
    "LocalEmbeddingSender",
]