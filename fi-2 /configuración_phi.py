# Copyright (c) Microsoft Corporation.
# Licenciado bajo la licencia MIT.

importar matematicas
al escribir importar  Opcional

desde transformadores importa PretrainedConfig


clase  PhiConfig ( PretrainedConfig ):
    """Configuración Phi."""

    tipo_modelo = "phi-msft"
    mapa_atributo = {
        "max_position_embeddings" : "n_posiciones" ,
        "hidden_size" : "n_embd" ,
        "num_attention_heads" : "n_head" ,
        "num_hidden_layers" : "n_capas" ,
    }

    def  __inicio__ (
        ser,
        tamaño_vocab: int = 50304 ,
        n_posiciones: int = 2048 ,
        n_embd: int = 1024 ,
        n_capa: int = 20 ,
        n_inner: Opcional [ int ] = Ninguno ,
        n_cabeza: int = 16 ,
        n_head_kv: Opcional [ int ] = Ninguno ,
        Rotary_dim: Opcional [ int ] = 32 ,
        función_activación: Opcional [ str ] = "gelu_new" ,
        flash_attn: bool = Falso ,
        flash_rotary: bool = Falso ,
        fusionado_denso: bool = Falso ,
        atención_pdrop: flotante = 0.0 ,
        embd_pdrop: flotador = 0.0 ,
        resid_pdrop: flotador = 0.0 ,
        capa_norm_epsilon: flotante = 1e-5 ,
        rango_inicializador: flotante = 0,02 ,
        tie_word_embeddings: bool = Falso ,
        pad_vocab_size_multiple: int = 64 ,
        **kwargs
    ) -> Ninguno :
        self.vocab_size = int (math.ceil(vocab_size / pad_vocab_size_multiple) * pad_vocab_size_multiple)
        self.n_posiciones = n_posiciones
        self.n_embd = n_embd
        self.n_capa = n_capa
        self.n_inner = n_inner
        self.n_head = n_cabeza
        self.n_head_kv = n_head_kv
        self.rotary_dim = min (rotary_dim, n_embd // n_head)
        self.activation_function = función_activación
        self.flash_attn = flash_attn
        self.flash_rotary = flash_rotary
        self.fused_dense = fusionado_denso
        self.attn_pdrop = atención_pdrop
        self.embd_pdrop = embd_pdrop
        self.resid_pdrop = resid_pdrop
        self.layer_norm_epsilon = capa_norm_epsilon
        self.initializer_range = rango_inicializador

        super ().__init__(tie_word_embeddings=tie_word_embeddings, **kwargs)
