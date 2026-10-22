import re

def analyze_content_relevance(text, primary_keywords, secondary_keywords):
    """
    Analyzes content for relevance based on keyword presence, density, and length.
    Simulates a simplified search engine content evaluation algorithm.
    """
    text_lower = text.lower()
    words = re.findall(r'\b\w+\b', text_lower)
    total_words = len(words)

    score = 0
    keyword_hits = {}

    # --- 1. Keyword Presence and Frequency ---
    # Computer Science approach: Iterate and count, assign weights to keywords.
    for keyword in primary_keywords:
        count = text_lower.count(keyword.lower())
        keyword_hits[keyword] = count
        score += count * 5  # Higher weight for primary keywords

    for keyword in secondary_keywords:
        count = text_lower.count(keyword.lower())
        keyword_hits[keyword] = count
        score += count * 2  # Lower weight for secondary keywords

    # --- 2. Keyword Density Check (for primary keywords) ---
    # Algorithmic thinking: Define optimal ranges and apply penalties/bonuses.
    if total_words > 0:
        primary_keyword_total_count = sum(keyword_hits[k] for k in primary_keywords)
        density = (primary_keyword_total_count / total_words) * 100

        if 1.0 <= density <= 3.0:
            score += 20  # Bonus for optimal density
        elif density > 5.0:
            score -= 30  # Penalty for keyword stuffing (over-optimization)
        elif density < 0.5:
            score -= 10  # Penalty for too low density
        elif 0.5 <= density <= 5.0:
            score += 5 # Small bonus for acceptable density

    # --- 3. Content Length ---
    # System analysis: Longer, comprehensive content often signals higher quality.
    if total_words >= 500:
        score += 30 # Significant bonus for substantial content
    elif total_words >= 200:
        score += 10 # Moderate bonus
    else:
        score -= 5 # Slight penalty for very short content

    # --- 4. Basic Structure/Readability (Simplified) ---
    # Problem-solving: How to quickly assess content quality signals.
    # Check for presence of multiple paragraphs (simple proxy: multiple newlines)
    if text.count('\n\n') >= 2:
        score += 5 # Bonus for structured content

    return score, keyword_hits, total_words

# --- Define Target Keywords for our "Search Engine" ---
TARGET_PRIMARY_KEYWORDS = ["seo", "içerik stratejisi", "dijital pazarlama"]
TARGET_SECONDARY_KEYWORDS = ["algoritma", "bilgisayar bilimleri", "optimizasyon", "arama motoru"]

# --- Sample Articles (simulating different content quality/focus) ---
articles = {
    "Article A: SEO Temelleri": """
    SEO (Arama Motoru Optimizasyonu), web sitelerinin arama motoru sonuç sayfalarında (SERP) daha üst sıralarda yer almasını sağlayan bir dizi tekniktir. Bu, dijital pazarlama stratejilerinin temel taşlarından biridir. İçerik stratejisi, kullanıcıların aradığı bilgiyi sunarak ve anahtar kelimeleri doğru şekilde kullanarak SEO performansını artırır. Algoritma güncellemeleri, SEO uzmanlarının sürekli olarak stratejilerini optimize etmelerini gerektirir. Bilgisayar bilimleri eğitimi alan birinin bu algoritma mantığını anlaması büyük avantaj sağlar. Optimizasyon sadece anahtar kelimelerle sınırlı değildir, aynı zamanda site hızı ve mobil uyumluluk gibi teknik faktörleri de içerir.
    """,
    "Article B: Genel Pazarlama İpuçları": """
    Bu makale, genel pazarlama ipuçları ve sosyal medya stratejileri hakkında bilgi vermektedir. Marka bilinirliği oluşturmak ve müşteri etkileşimini artırmak için çeşitli yöntemler ele alınmıştır. Dijital reklamcılık ve e-posta pazarlaması da önemli konulardır. İşletmelerin online varlıklarını güçlendirmeleri için pratik tavsiyeler sunulmaktadır. Başarılı bir kampanya yürütmek için hedef kitle analizi şarttır.
    """,
    "Article C: Derinlemesine İçerik Stratejisi": """
    Etkili bir içerik stratejisi geliştirmek, sadece anahtar kelimeleri doldurmaktan çok daha fazlasını gerektirir. Kullanıcı niyeti, içerik türleri ve dağıtım kanalları gibi faktörler göz önünde bulundurulmalıdır. Arama motoru algoritmaları, kaliteli ve değerli içeriği ödüllendirir. Bu nedenle, bilgisayar bilimleri kökenli bir analitik yaklaşım, içerik optimizasyonunda kritik rol oynar. SEO, bu stratejinin ayrılmaz bir parçasıdır. Veri analizi ve algoritmik düşünme, içerik performansını sürekli iyileştirmek için temel araçlardır. Optimizasyon süreçleri, sürekli test ve öğrenmeyi içerir.
    """,
    "Article D: Keyword Stuffing Örneği": """
    SEO SEO SEO. Bu makale SEO hakkında. SEO stratejileri çok önemli. Dijital pazarlama için SEO şart. İçerik stratejisi SEO ile başlar. SEO optimizasyon SEO. Arama motoru SEO. Bilgisayar bilimleri SEO. Algoritma SEO. SEO SEO SEO.
    """
}

# --- Evaluate Articles ---
print("--- Content Relevance Analysis ---")
print(f"Target Primary Keywords: {', '.join(TARGET_PRIMARY_KEYWORDS)}")
print(f"Target Secondary Keywords: {', '.join(TARGET_SECONDARY_KEYWORDS)}\n")

results = []
for title, content in articles.items():
    score, hits, word_count = analyze_content_relevance(
        content, TARGET_PRIMARY_KEYWORDS, TARGET_SECONDARY_KEYWORDS
    )
    results.append({"title": title, "score": score, "keyword_hits": hits, "word_count": word_count})
    
    print(f"Article: {title}")
    print(f"  Total Words: {word_count}")
    print(f"  Keyword Hits: {hits}")
    print(f"  Relevance Score: {score}\n")

# --- Rank Articles ---
# Computer Science application: Sorting algorithms for ranking.
ranked_results = sorted(results, key=lambda x: x["score"], reverse=True)

print("\n--- Ranked Articles by Relevance Score ---")
for i, item in enumerate(ranked_results):
    print(f"{i+1}. {item['title']} (Score: {item['score']})")
