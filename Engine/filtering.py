import warnings
from numba.core.errors import NumbaTypeSafetyWarning
from bm25_fusion import BM25
from bm25_fusion.tokenization import tokenize

def filt(articles):
    warnings.simplefilter('ignore', category=NumbaTypeSafetyWarning)
    
    if not articles:
        return []

    corpus = [item.get('description') or '' for item in articles]
    metadata = [item for item in articles]

    stopwords = {'is', 'a', 'the', 'and'}
    bm25 = BM25(metadata=metadata, texts=corpus, variant='bm25+', delta=0.5, stopwords=stopwords)
    
    query = "finance stock market earnings"
    results = bm25.query(query, top_k=4)

    bm25.save_hdf5('bm_model.h5')
    return results