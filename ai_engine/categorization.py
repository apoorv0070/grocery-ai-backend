def auto_categorize_product(name, description=''):
    n = (name or '').lower()
    if 'milk' in n: return 'Dairy'
    if 'apple' in n: return 'Fruits'
    return 'Uncategorized'
