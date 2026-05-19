import re

file_path = 'index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Meta and Title
content = content.replace(
    '<title>Mahindra Vista Kandivali East | Premium 2, 3 & 4 BHK Apartments</title>',
    '<title>New Phase Launch at Rustomjee Ozone Goregaon West</title>'
)
content = content.replace(
    'content="Mahindra Vista Kandivali East is a premium residential project located in the heart of Mumbai. Designed to offer modern living, it combines stylish architecture with green surroundings."',
    'content="New Phase Launch at Rustomjee Ozone Goregaon West. Premium 2 & 3 BHK Apartments in Goregaon West New Launch. Exclusive Pre-Launch Opportunity at Rustomjee Ozone."'
)
content = content.replace(
    'content="Mahindra Vista, Kandivali East, Premium apartments, 2 BHK Kandivali, 3 BHK Kandivali, 4 BHK Kandivali, Mahindra Lifespaces, Luxury homes Mumbai, Eco-friendly community"',
    'content="Rustomjee Ozone new phase, Goregaon West new tower launch, Pre-launch benefits Rustomjee Ozone, G+49 luxury tower Goregaon West, 2 BHK 3 BHK flat SV Road, NeoLiv Goregaon West project"'
)
content = content.replace(
    '<meta name="author" content="Mahindra Group">',
    '<meta name="author" content="NeoLiv Group">'
)

# Nav Logo
content = content.replace('alt="Mahindra Vista"', 'alt="Rustomjee Ozone"')

# Hero Section
content = re.sub(
    r'Mahindra\s*Vista, <br>\s*<p class="text-sm text-gray-700 text-center mb-4 font-semibold uppercase tracking-wider">\s*At Kandivali East\s*</p>',
    r'Rustomjee Ozone, <br>  <p class="text-sm text-gray-700 text-center mb-4 font-semibold uppercase tracking-wider">\n                          At SV Road, Mahesh Nagar, Goregaon West   </p>',
    content
)
content = content.replace(
    'By Mahindra LifeSpaces',
    'New Tower By NeoLiv Group & Trusted Construction Partners'
)

# Hero Info Boxes
content = content.replace(
    '<p class="text-sm text-gray-500 uppercase tracking-wider">Land Parcel</p>\n                                <p class="font-bold text-gray-800">3.53 Acres</p>',
    '<p class="text-sm text-gray-500 uppercase tracking-wider">Configuration</p>\n                                <p class="font-bold text-gray-800">2 & 3 BHK</p>'
)
content = content.replace(
    '<p class="text-xs text-gray-600 text-center">Towers</p>\n                                <p class="text-center text-black font-bold">5 Towers</p>',
    '<p class="text-xs text-gray-600 text-center">Elevation</p>\n                                <p class="text-center text-black font-bold">G+49 Storeys</p>'
)
content = content.replace(
    '<p class="text-sm text-gray-500 uppercase tracking-wider">Possession</p>\n                                <p class="text-sm font-bold text-gray-800">December 2028 *</p>',
    '<p class="text-sm text-gray-500 uppercase tracking-wider">RERA No</p>\n                                <p class="text-sm font-bold text-gray-800">Coming Soon</p>'
)

# CTA text
content = content.replace(
    '<p> Avail early bird benefits</p>\n                            <p> Get Choice of Inventory</p>\n                            <p> Avail spot booking offers & Best Price</p>',
    '<p> Get Pre-Launch Benefits</p>\n                            <p> Avail Early Bird Offer</p>\n                            <p> Spot Booking Offers Available & Best Price Guaranteed</p>'
)

# Hero Price
content = content.replace(
    'Lavish 2, 3 & 4 BHK residences <br>\n                                <span class="text-base font-medium text-gray-700">Starting From <br> <strong\n                                        style="font-size: 22px">₹ 1.86 Cr All Inclusive</strong></span>',
    'Premium 2 & 3 BHK Apartments <br>\n                                <span class="text-base font-medium text-gray-700">Starting From <br> <strong\n                                        style="font-size: 22px">₹ 2.50 Cr All Inclusive</strong></span>'
)

# Highlights Intro
content = content.replace(
    '<h2 class="font-heading text-4xl md:text-5xl font-bold text-navy mb-4">Mahindra Vista Kandivali Highlights</h2>',
    '<h2 class="font-heading text-4xl md:text-5xl font-bold text-navy mb-4">Rustomjee Ozone Goregaon Highlights</h2>'
)
content = content.replace(
    '<p class="text-xl text-gray-600 max-w-2xl mx-auto font-body">Exceptional features that define luxury living in Kandivali East. 50+ Modern Amenities.</p>',
    '<p class="text-xl text-gray-600 max-w-2xl mx-auto font-body">Premium high-rise living with rooftop amenities on SV Road. Best gated community high-rise under pre-launch pricing in Goregaon West.</p>'
)

# Replace highlight cards 
old_cards = '''                    <div class="glass-card p-8 rounded-3xl border border-white/50 shadow-xl hover:shadow-2xl transition-all duration-500 group reveal">
                        <div class="w-16 h-16 bg-gold/10 rounded-2xl flex items-center justify-center mb-6 group-hover:bg-gold/20 transition-colors">
                            <i data-lucide="users" class="text-gold w-8 h-8"></i>
                        </div>
                        <h3 class="font-heading text-xl font-bold text-navy mb-3">Roof Clubhouse & Greens</h3>
                        <p class="text-gray-600 leading-relaxed">State of the Art <b> 28,000 Sq.Ft. </b> Roof Clubhouse | 1.92 Acres of Landscaped Greens</p>
                    </div>

                    <!-- Highlight 2 -->
                    <div class="glass-card p-8 rounded-3xl border border-white/50 shadow-xl hover:shadow-2xl transition-all duration-500 group reveal" style="transition-delay: 100ms">
                        <div class="w-16 h-16 bg-accent/10 rounded-2xl flex items-center justify-center mb-6 group-hover:bg-accent/20 transition-colors">
                            <i data-lucide="sparkles" class="text-accent w-8 h-8"></i>
                        </div>
                        <h3 class="font-heading text-xl font-bold text-navy mb-3">Luxury Living</h3>
                        <p class="text-gray-600 leading-relaxed">Designed With Infinity Edge Pool | Vitrified Tiles in Living & Dining Room</p>
                    </div>

                    <!-- Highlight 3 -->
                    <div class="glass-card p-8 rounded-3xl border border-white/50 shadow-xl hover:shadow-2xl transition-all duration-500 group reveal" style="transition-delay: 200ms">
                        <div class="w-16 h-16 bg-navy/10 rounded-2xl flex items-center justify-center mb-6 group-hover:bg-navy/20 transition-colors">
                            <i data-lucide="leaf" class="text-navy w-8 h-8"></i>
                        </div>
                        <h3 class="font-heading text-xl font-bold text-navy mb-3">Net Zero Homes</h3>
                        <p class="text-gray-600 leading-relaxed"><b>India's 1st </b> Net Zero Waste + Energy Homes | High Street & Retail at Your Doorstep</p>
                    </div>

                    <!-- Highlight 4 -->
                    <div class="glass-card p-8 rounded-3xl border border-white/50 shadow-xl hover:shadow-2xl transition-all duration-500 group reveal" style="transition-delay: 300ms">
                        <div class="w-16 h-16 bg-gold/10 rounded-2xl flex items-center justify-center mb-6 group-hover:bg-gold/20 transition-colors">
                            <i data-lucide="home" class="text-gold w-8 h-8"></i>
                        </div>
                        <h3 class="font-heading text-xl font-bold text-navy mb-3">Premium Residences</h3>
                        <p class="text-gray-600 leading-relaxed">Efficient <b>2, 3, and 4 BHK   Premium Residences</b> With Balconies</p>
                    </div>

                    <!-- Highlight 5 -->
                    <div class="glass-card p-8 rounded-3xl border border-white/50 shadow-xl hover:shadow-2xl transition-all duration-500 group reveal" style="transition-delay: 400ms">
                        <div class="w-16 h-16 bg-accent/10 rounded-2xl flex items-center justify-center mb-6 group-hover:bg-accent/20 transition-colors">
                            <i data-lucide="layers" class="text-accent w-8 h-8"></i>
                        </div>
                        <h3 class="font-heading text-xl font-bold text-navy mb-3">Signature Podium</h3>
                        <p class="text-gray-600 leading-relaxed">Signature Designed Colonnade With an <b>Infinity Edge Pool</b> on a 1.6 Acre Podium</p>
                    </div>

                    <!-- Highlight 6 -->
                    <div class="glass-card p-8 rounded-3xl border border-white/50 shadow-xl hover:shadow-2xl transition-all duration-500 group reveal" style="transition-delay: 500ms">
                        <div class="w-16 h-16 bg-navy/10 rounded-2xl flex items-center justify-center mb-6 group-hover:bg-navy/20 transition-colors">
                            <i data-lucide="shopping-bag" class="text-navy w-8 h-8"></i>
                        </div>
                        <h3 class="font-heading text-xl font-bold text-navy mb-3">Convenient Retail</h3>
                        <p class="text-gray-600 leading-relaxed">High Street and Convenient Retail at Your Doorstep</p>
                    </div>'''

new_cards = '''                    <!-- Highlight 1 -->
                    <div class="glass-card p-8 rounded-3xl border border-white/50 shadow-xl hover:shadow-2xl transition-all duration-500 group reveal">
                        <div class="w-16 h-16 bg-gold/10 rounded-2xl flex items-center justify-center mb-6 group-hover:bg-gold/20 transition-colors">
                            <i data-lucide="users" class="text-gold w-8 h-8"></i>
                        </div>
                        <h3 class="font-heading text-xl font-bold text-navy mb-3">Impeccable Construction</h3>
                        <p class="text-gray-600 leading-relaxed">Rustomjee Standard Finish with exquisite blend of sophisticated urban planning.</p>
                    </div>

                    <!-- Highlight 2 -->
                    <div class="glass-card p-8 rounded-3xl border border-white/50 shadow-xl hover:shadow-2xl transition-all duration-500 group reveal" style="transition-delay: 100ms">
                        <div class="w-16 h-16 bg-accent/10 rounded-2xl flex items-center justify-center mb-6 group-hover:bg-accent/20 transition-colors">
                            <i data-lucide="sparkles" class="text-accent w-8 h-8"></i>
                        </div>
                        <h3 class="font-heading text-xl font-bold text-navy mb-3">Rooftop Deck</h3>
                        <p class="text-gray-600 leading-relaxed">State-of-the-Art fitness and recreation amenities situated spectacularly on the topmost <b>49th level</b>.</p>
                    </div>

                    <!-- Highlight 3 -->
                    <div class="glass-card p-8 rounded-3xl border border-white/50 shadow-xl hover:shadow-2xl transition-all duration-500 group reveal" style="transition-delay: 200ms">
                        <div class="w-16 h-16 bg-navy/10 rounded-2xl flex items-center justify-center mb-6 group-hover:bg-navy/20 transition-colors">
                            <i data-lucide="leaf" class="text-navy w-8 h-8"></i>
                        </div>
                        <h3 class="font-heading text-xl font-bold text-navy mb-3">Efficient Layouts</h3>
                        <p class="text-gray-600 leading-relaxed">Highly Efficient 2 BHK & 3 BHK sizing designed for those who seek an elite lifestyle.</p>
                    </div>

                    <!-- Highlight 4 -->
                    <div class="glass-card p-8 rounded-3xl border border-white/50 shadow-xl hover:shadow-2xl transition-all duration-500 group reveal" style="transition-delay: 300ms">
                        <div class="w-16 h-16 bg-gold/10 rounded-2xl flex items-center justify-center mb-6 group-hover:bg-gold/20 transition-colors">
                            <i data-lucide="home" class="text-gold w-8 h-8"></i>
                        </div>
                        <h3 class="font-heading text-xl font-bold text-navy mb-3">Investment Goldmine</h3>
                        <p class="text-gray-600 leading-relaxed">High End-User Demand & Massive Rental Yield Potential.</p>
                    </div>

                    <!-- Highlight 5 -->
                    <div class="glass-card p-8 rounded-3xl border border-white/50 shadow-xl hover:shadow-2xl transition-all duration-500 group reveal" style="transition-delay: 400ms">
                        <div class="w-16 h-16 bg-accent/10 rounded-2xl flex items-center justify-center mb-6 group-hover:bg-accent/20 transition-colors">
                            <i data-lucide="layers" class="text-accent w-8 h-8"></i>
                        </div>
                        <h3 class="font-heading text-xl font-bold text-navy mb-3">Excellent Connectivity</h3>
                        <p class="text-gray-600 leading-relaxed">Strategically positioned along the high-growth SV Road corridor in Mahesh Nagar.</p>
                    </div>

                    <!-- Highlight 6 -->
                    <div class="glass-card p-8 rounded-3xl border border-white/50 shadow-xl hover:shadow-2xl transition-all duration-500 group reveal" style="transition-delay: 500ms">
                        <div class="w-16 h-16 bg-navy/10 rounded-2xl flex items-center justify-center mb-6 group-hover:bg-navy/20 transition-colors">
                            <i data-lucide="shopping-bag" class="text-navy w-8 h-8"></i>
                        </div>
                        <h3 class="font-heading text-xl font-bold text-navy mb-3">Exclusive New Phase</h3>
                        <p class="text-gray-600 leading-relaxed">Exclusive New Phase Inventory Release. Best Pre-Launch Price Guaranteed.</p>
                    </div>'''
content = content.replace(old_cards, new_cards)

# About Section
old_about = '''                    <div>
                        <h2 class="font-heading text-3xl md:text-5xl font-bold text-navy mb-6">About <span class="text-accent">Mahindra Vista</span> Kandivali East</h2>
                        <p class="text-lg text-gray-700 mb-6 font-body leading-relaxed">
                            <span class="font-bold text-navy">Mahindra Vista Kandivali East</span> is a premium residential project located in the heart of Mumbai, offering meticulously crafted <span class="font-bold text-navy">2, 3 & 4 BHK residences</span>. Designed to offer modern living, it combines stylish architecture with <span class="text-accent font-semibold">1.92 acres of landscaped greens</span> and features India's 1st <span class="text-accent font-semibold">Net Zero Waste + Energy Homes</span>. The project boasts a massive <span class="text-accent font-semibold">28,000 Sq.Ft. roof clubhouse</span> and a <span class="text-accent font-semibold">1.6-acre podium</span> with an infinity edge pool, ensuring maximum comfort and luxury for families. This development brings a perfect balance of lifestyle and convenience, making it an ideal choice for homebuyers in Mumbai.
                        </p>
                        <p class="text-lg text-gray-700 mb-8 font-body leading-relaxed">
                            This property is one of the visionary projects of <span class="font-bold text-navy">Mahindra Lifespaces</span>. The one-of-its-kind residential project is thoughtfully designed by harnessing the power of nature and innovation.
                        </p>
                        <div class="grid grid-cols-2 gap-6">
                            <div class="glass-card p-6 rounded-2xl border border-gray-100 shadow-sm hover:shadow-md transition-all">
                                <h4 class="font-semibold text-accent mb-2 uppercase tracking-wider text-sm">Homes Delivered</h4>
                                <p class="text-3xl font-bold text-navy">9,800+</p>
                            </div>
                            <div class="glass-card p-6 rounded-2xl border border-gray-100 shadow-sm hover:shadow-md transition-all">
                                <h4 class="font-semibold text-accent mb-2 uppercase tracking-wider text-sm">Project Area</h4>
                                <p class="text-3xl font-bold text-navy">3.53 Acres</p>
                            </div>
                        </div>'''

new_about = '''                    <div>
                        <h2 class="font-heading text-3xl md:text-5xl font-bold text-navy mb-6">The New Standard of Luxury: <br><span class="text-accent">Rustomjee Ozone</span> (New Phase)</h2>
                        <p class="text-lg text-gray-700 mb-6 font-body leading-relaxed">
                            Discover a rare opportunity to own a piece of the future in Mumbai's most vibrant premium micro-market. Strategically positioned along the high-growth SV Road corridor in Mahesh Nagar, Goregaon West, the <span class="font-bold text-navy">New Phase at Rustomjee Ozone</span> offers an exquisite blend of sophisticated urban planning and elevated vertical living. This premium G+49 high-rise residential tower is designed for those who seek an elite lifestyle, featuring an architectural redevelopment benchmark under DCR 33(10) and the signature quality of a trusted Rustomjee standard finish.
                        </p>
                        <p class="text-lg text-gray-700 mb-8 font-body leading-relaxed">
                            With all primary modern fitness and recreation amenities situated spectacularly on the topmost 49th level, residents will enjoy panoramic views of the city skyline away from the hustle below. As major transit infrastructures like the Goregaon-Mulund Link Road (GMLR) and the Versova-Dahisar Coastal Road advance, this new phase stands at the heart of an investment goldmine.
                        </p>'''
content = content.replace(old_about, new_about)

# Pricing Section
content = content.replace(
    'Mahindra Vista Kandivali East - Pricing Plans',
    'Rustomjee Ozone Goregaon - Pricing Plans'
)

old_pricing = '''                <!-- Pricing Cards -->
                <div class="grid grid-cols-1 md:grid-cols-3 gap-8 reveal">
                    <!-- 2 BHK Card -->
                    <div class="glass-card rounded-3xl border border-gold/20 p-8 shadow-xl hover:shadow-2xl transition-all hover:-translate-y-2 group">
                        <div class="mb-6 text-center">
                            <h3 class="text-3xl font-bold text-navy">2 BHK Residence</h3>
                            <div class="w-12 h-1 bg-gold mx-auto mt-2"></div>
                        </div>
                        <div class="space-y-4 mb-8">
                            <div class="flex justify-between items-center border-b border-gray-100 pb-2">
                                <span class="text-gray-600 font-medium">Carpet Area</span>
                                <span class="font-bold text-navy">600 - 813 SQ.FT</span>
                            </div>
                            <div class="text-center pt-2">
                                <span class="text-gray-500 text-sm block mb-1">Starting From</span>
                                <span class="text-3xl font-extrabold text-accent">₹ 1.62 Cr*</span>
                            </div>
                        </div>
                        <button onclick="openPopup('Price List 2 BHK')" class="w-full animated-gradient-button text-white py-4 rounded-xl font-bold transform transition-all group-hover:scale-105 shadow-lg shadow-accent/20">
                            Get Details
                        </button>
                    </div>

                    <!-- 3 BHK Card -->
                    <div class="glass-card rounded-3xl border border-gold/20 p-8 shadow-xl hover:shadow-2xl transition-all hover:-translate-y-2 group">
                        <div class="mb-6 text-center">
                            <h3 class="text-3xl font-bold text-navy">3 BHK Residence</h3>
                            <div class="w-12 h-1 bg-gold mx-auto mt-2"></div>
                        </div>
                        <div class="space-y-4 mb-8">
                            <div class="flex justify-between items-center border-b border-gray-100 pb-2">
                                <span class="text-gray-600 font-medium">Carpet Area</span>
                                <span class="font-bold text-navy">934 - 1061 SQ.FT</span>
                            </div>
                            <div class="text-center pt-2">
                                <span class="text-gray-500 text-sm block mb-1">Starting From</span>
                                <span class="text-3xl font-extrabold text-accent">₹ 2.55 Cr*</span>
                            </div>
                        </div>
                        <button onclick="openPopup('Price List 3 BHK')" class="w-full animated-gradient-button text-white py-4 rounded-xl font-bold transform transition-all group-hover:scale-105 shadow-lg shadow-accent/20">
                            Get Details
                        </button>
                    </div>

                    <!-- 4 BHK Card -->
                    <div class="glass-card rounded-3xl border border-gold/20 p-8 shadow-xl hover:shadow-2xl transition-all hover:-translate-y-2 group">
                        <div class="mb-6 text-center">
                            <h3 class="text-3xl font-bold text-navy">4 BHK Residence</h3>
                            <div class="w-12 h-1 bg-gold mx-auto mt-2"></div>
                        </div>
                        <div class="space-y-4 mb-8">
                            <div class="flex justify-between items-center border-b border-gray-100 pb-2">
                                <span class="text-gray-600 font-medium">Carpet Area</span>
                                <span class="font-bold text-navy">1624 SQ.FT</span>
                            </div>
                            <div class="text-center pt-2">
                                <span class="text-gray-500 text-sm block mb-1">Starting From</span>
                                <span class="text-3xl font-extrabold text-accent">₹ 3.90 Cr*</span>
                            </div>
                        </div>
                        <button onclick="openPopup('Price List 4 BHK')" class="w-full animated-gradient-button text-white py-4 rounded-xl font-bold transform transition-all group-hover:scale-105 shadow-lg shadow-accent/20">
                            Get Details
                        </button>
                    </div>
                </div>'''

new_pricing = '''                <!-- Pricing Cards -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8 reveal max-w-4xl mx-auto">
                    <!-- 2 BHK Card -->
                    <div class="glass-card rounded-3xl border border-gold/20 p-8 shadow-xl hover:shadow-2xl transition-all hover:-translate-y-2 group">
                        <div class="mb-6 text-center">
                            <h3 class="text-3xl font-bold text-navy">2 BHK (New Phase)</h3>
                            <div class="w-12 h-1 bg-gold mx-auto mt-2"></div>
                        </div>
                        <div class="space-y-4 mb-8">
                            <div class="flex justify-between items-center border-b border-gray-100 pb-2">
                                <span class="text-gray-600 font-medium">Carpet Area</span>
                                <span class="font-bold text-navy">740 Sq.Ft.</span>
                            </div>
                            <div class="text-center pt-2">
                                <span class="text-gray-500 text-sm block mb-1">Starting From</span>
                                <span class="text-3xl font-extrabold text-accent">₹ 2.50 Cr*</span>
                            </div>
                        </div>
                        <button onclick="openPopup('Price List 2 BHK')" class="w-full animated-gradient-button text-white py-4 rounded-xl font-bold transform transition-all group-hover:scale-105 shadow-lg shadow-accent/20">
                            Get Details
                        </button>
                    </div>

                    <!-- 3 BHK Card -->
                    <div class="glass-card rounded-3xl border border-gold/20 p-8 shadow-xl hover:shadow-2xl transition-all hover:-translate-y-2 group">
                        <div class="mb-6 text-center">
                            <h3 class="text-3xl font-bold text-navy">3 BHK (New Phase)</h3>
                            <div class="w-12 h-1 bg-gold mx-auto mt-2"></div>
                        </div>
                        <div class="space-y-4 mb-8">
                            <div class="flex justify-between items-center border-b border-gray-100 pb-2">
                                <span class="text-gray-600 font-medium">Carpet Area</span>
                                <span class="font-bold text-navy">980 Sq.Ft.</span>
                            </div>
                            <div class="text-center pt-2">
                                <span class="text-gray-500 text-sm block mb-1">Starting From</span>
                                <span class="text-3xl font-extrabold text-accent">₹ 3.45 Cr*</span>
                            </div>
                        </div>
                        <button onclick="openPopup('Price List 3 BHK')" class="w-full animated-gradient-button text-white py-4 rounded-xl font-bold transform transition-all group-hover:scale-105 shadow-lg shadow-accent/20">
                            Get Details
                        </button>
                    </div>
                </div>'''
content = content.replace(old_pricing, new_pricing)

# Floor plans
content = content.replace(
    'Mahindra Vista Kandivali East Master & Floor Plans',
    'Rustomjee Ozone Master & Floor Plans'
)

# Amenities
content = re.sub(r'Mahindra Vista Kandivali East\s*-\s*Amenities', 'Rustomjee Ozone Goregaon - Amenities', content)

# Gallery
content = re.sub(r'Mahindra Vista Kandivali East\s*-\s*<span class="text-gold">Gallery</span>', 'Rustomjee Ozone - <span class="text-gold">Gallery</span>', content)

# Location
content = content.replace(
    'Located in the heart of Kandivali East, offering seamless access to Mumbai\\'s primary hubs.',
    'Located in the heart of Goregaon West, offering seamless access to Mumbai\\'s primary hubs.'
)

old_location_cards = '''                        <div class="grid sm:grid-cols-2 gap-4">
                            <!-- Connectivity -->
                            <div class="glass-card-dark p-6 rounded-2xl section-reveal"
                                style="transition-delay: 100ms;">
                                <div class="w-12 h-12 bg-gold/20 rounded-xl flex items-center justify-center mb-4">
                                    <i data-lucide="train" class="text-gold w-6 h-6"></i>
                                </div>
                                <h4 class="text-white font-bold mb-3">Transit Hubs</h4>
                                <ul class="space-y-2 text-sm text-gray-200">
                                    <li class="flex justify-between"><span class="text-white">Akurli Metro Station</span> <span
                                            class="text-gold font-semibold">1 km</span></li>
                                    <li class="flex justify-between"><span class="text-white">Poinsur (Poisar) Metro Station</span> <span
                                            class="text-gold font-semibold">1.2 km</span></li>
                                    <li class="flex justify-between"><span class="text-white">Kandivali Railway Station</span> <span
                                            class="text-gold font-semibold">3.2 km</span></li>
                                    <li class="flex justify-between"><span class="text-white">Borivali Railway Station</span> <span
                                            class="text-gold font-semibold">4.5 km</span></li>
                                    <li class="flex justify-between"><span class="text-white">Western Express Highway</span> <span
                                            class="text-gold font-semibold">1 km</span></li>
                                    <li class="flex justify-between"><span class="text-white">Akurli Road</span> <span
                                            class="text-gold font-semibold">500 m</span></li>
                                </ul>
                            </div>

                            <!-- Education -->
                            <div class="glass-card-dark p-6 rounded-2xl section-reveal"
                                style="transition-delay: 200ms;">
                                <div class="w-12 h-12 bg-accent/20 rounded-xl flex items-center justify-center mb-4">
                                    <i data-lucide="graduation-cap" class="text-accent w-6 h-6"></i>
                                </div>
                                <h4 class="text-white font-bold mb-3">Education</h4>
                                <ul class="space-y-2 text-sm text-gray-300">
                                    <li class="flex justify-between"><span>Lokhandwala Foundation School</span> <span
                                            class="text-gold font-semibold">700 m</span></li>
                                    <li class="flex justify-between"><span>Oxford International School</span> <span
                                            class="text-gold font-semibold">950 m</span></li>
                                    <li class="flex justify-between"><span>Cambridge School ICSE</span> <span
                                            class="text-gold font-semibold">2 km</span></li>
                                    <li class="flex justify-between"><span>Oberoi International School</span> <span
                                            class="text-gold font-semibold">4.5 km</span></li>
                                    <li class="flex justify-between"><span>Thakur International School</span> <span
                                            class="text-gold font-semibold">4 km</span></li>
                                    <li class="flex justify-between"><span>KES International School</span> <span
                                            class="text-gold font-semibold">2.8 km</span></li>
                                </ul>
                            </div>

                            <!-- HealthCare -->
                            <div class="glass-card-dark p-6 rounded-2xl section-reveal"
                                style="transition-delay: 300ms;">
                                <div class="w-12 h-12 bg-blue-500/20 rounded-xl flex items-center justify-center mb-4">
                                    <i data-lucide="hospital" class="text-blue-400 w-6 h-6"></i>
                                </div>
                                <h4 class="text-white font-bold mb-3">Healthcare</h4>
                                <ul class="space-y-2 text-sm text-gray-300">
                                    <li class="flex justify-between"><span>Seven Star Multispeciality Hospital</span> <span
                                            class="text-gold font-semibold">2.1 km</span></li>
                                    <li class="flex justify-between"><span>DNA Multispeciality Hospital</span> <span
                                            class="text-gold font-semibold">3.4 km</span></li>
                                    <li class="flex justify-between"><span>Shreeji Hospital</span> <span
                                            class="text-gold font-semibold">550 m</span></li>
                                    <li class="flex justify-between"><span>Ozone Therapy Centre</span> <span
                                            class="text-gold font-semibold">550 m</span></li>
                                    <li class="flex justify-between"><span>Akurli Maternity Home</span> <span
                                            class="text-gold font-semibold">900 m</span></li>
                                </ul>
                            </div>

                            <!-- Retail -->
                            <div class="glass-card-dark p-6 rounded-2xl section-reveal"
                                style="transition-delay: 400ms;">
                                <div class="w-12 h-12 bg-green-500/20 rounded-xl flex items-center justify-center mb-4">
                                    <i data-lucide="shopping-cart" class="text-green-400 w-6 h-6"></i>
                                </div>
                                <h4 class="text-white font-bold mb-3">Retail</h4>
                                <ul class="space-y-2 text-sm text-gray-200">
                                    <li class="flex justify-between"><span class="text-white">Growel’s 101 Mall</span> <span
                                            class="text-gold font-semibold">1.9 km</span></li>
                                    <li class="flex justify-between"><span class="text-white">Oberoi Mall</span> <span
                                            class="text-gold font-semibold">4 km</span></li>
                                    <li class="flex justify-between"><span class="text-white">Infiniti Mall</span> <span
                                            class="text-gold font-semibold">5.5 km</span></li>
                                    <li class="flex justify-between"><span class="text-white">Eastern Plaza / Malad Mall</span> <span
                                            class="text-gold font-semibold">3.2 km</span></li>
                                </ul>
                            </div>

                            <!-- Parks -->
                            <div class="glass-card-dark p-6 rounded-2xl section-reveal"
                                style="transition-delay: 500ms;">
                                <div class="w-12 h-12 bg-emerald-500/20 rounded-xl flex items-center justify-center mb-4">
                                    <i data-lucide="trees" class="text-emerald-400 w-6 h-6"></i>
                                </div>
                                <h4 class="text-white font-bold mb-3">Parks</h4>
                                <ul class="space-y-2 text-sm text-gray-200">
                                    <li class="flex justify-between"><span class="text-white">Shaheed Bhagat Singh Park</span> <span
                                            class="text-gold font-semibold">1.6 km</span></li>
                                    <li class="flex justify-between"><span class="text-white">Thakur Stadium MCGM Ground</span> <span
                                            class="text-gold font-semibold">1.4 km</span></li>
                                    <li class="flex justify-between"><span class="text-white">Foundation Ground</span> <span
                                            class="text-gold font-semibold">800 m</span></li>
                                    <li class="flex justify-between"><span class="text-white">Lokhandwala Joggers Park</span> <span
                                            class="text-gold font-semibold">550 m</span></li>
                                </ul>
                            </div>
                        </div>'''

new_location_cards = '''                        <div class="grid sm:grid-cols-2 gap-4">
                            <!-- Connectivity -->
                            <div class="glass-card-dark p-6 rounded-2xl section-reveal"
                                style="transition-delay: 100ms;">
                                <div class="w-12 h-12 bg-gold/20 rounded-xl flex items-center justify-center mb-4">
                                    <i data-lucide="train" class="text-gold w-6 h-6"></i>
                                </div>
                                <h4 class="text-white font-bold mb-3">Transit Hubs</h4>
                                <ul class="space-y-2 text-sm text-gray-200">
                                    <li class="flex justify-between"><span class="text-white">SV Road / Mahesh Nagar</span> <span
                                            class="text-gold font-semibold">Immediate</span></li>
                                    <li class="flex justify-between"><span class="text-white">Western Express Highway</span> <span
                                            class="text-gold font-semibold">5 Mins</span></li>
                                    <li class="flex justify-between"><span class="text-white">Goregaon Railway Station</span> <span
                                            class="text-gold font-semibold">1.7 km</span></li>
                                    <li class="flex justify-between"><span class="text-white">Lower Malad Metro</span> <span
                                            class="text-gold font-semibold">5 Mins</span></li>
                                </ul>
                            </div>

                            <!-- Education -->
                            <div class="glass-card-dark p-6 rounded-2xl section-reveal"
                                style="transition-delay: 200ms;">
                                <div class="w-12 h-12 bg-accent/20 rounded-xl flex items-center justify-center mb-4">
                                    <i data-lucide="graduation-cap" class="text-accent w-6 h-6"></i>
                                </div>
                                <h4 class="text-white font-bold mb-3">Education</h4>
                                <ul class="space-y-2 text-sm text-gray-300">
                                    <li class="flex justify-between"><span>D.G. Khetan Int. School</span> <span
                                            class="text-gold font-semibold">Walking</span></li>
                                    <li class="flex justify-between"><span>Ryan International School</span> <span
                                            class="text-gold font-semibold">Nearby</span></li>
                                    <li class="flex justify-between"><span>Oberoi International School</span> <span
                                            class="text-gold font-semibold">10 Mins</span></li>
                                </ul>
                            </div>

                            <!-- HealthCare -->
                            <div class="glass-card-dark p-6 rounded-2xl section-reveal"
                                style="transition-delay: 300ms;">
                                <div class="w-12 h-12 bg-blue-500/20 rounded-xl flex items-center justify-center mb-4">
                                    <i data-lucide="hospital" class="text-blue-400 w-6 h-6"></i>
                                </div>
                                <h4 class="text-white font-bold mb-3">Healthcare</h4>
                                <ul class="space-y-2 text-sm text-gray-300">
                                    <li class="flex justify-between"><span>Lifeline Medicare Hospital</span> <span
                                            class="text-gold font-semibold">Nearby</span></li>
                                    <li class="flex justify-between"><span>Zenith Multi-Speciality</span> <span
                                            class="text-gold font-semibold">Nearby</span></li>
                                </ul>
                            </div>

                            <!-- Retail -->
                            <div class="glass-card-dark p-6 rounded-2xl section-reveal"
                                style="transition-delay: 400ms;">
                                <div class="w-12 h-12 bg-green-500/20 rounded-xl flex items-center justify-center mb-4">
                                    <i data-lucide="shopping-cart" class="text-green-400 w-6 h-6"></i>
                                </div>
                                <h4 class="text-white font-bold mb-3">Retail & Hubs</h4>
                                <ul class="space-y-2 text-sm text-gray-200">
                                    <li class="flex justify-between"><span class="text-white">Inorbit Mall</span> <span
                                            class="text-gold font-semibold">10 Mins</span></li>
                                    <li class="flex justify-between"><span class="text-white">Infiniti Mall</span> <span
                                            class="text-gold font-semibold">10 Mins</span></li>
                                    <li class="flex justify-between"><span class="text-white">Oberoi Mall</span> <span
                                            class="text-gold font-semibold">10 Mins</span></li>
                                    <li class="flex justify-between"><span class="text-white">Mindspace IT Hub</span> <span
                                            class="text-gold font-semibold">Nearby</span></li>
                                </ul>
                            </div>
                        </div>'''

content = content.replace(old_location_cards, new_location_cards)

content = content.replace(
    'src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3768.182470701146!2d72.868744!3d19.201234!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3be7b738e4a7b7a1%3A0x8f8c8c8c8c8c8c8c!2sMahindra%20Lifespaces%20Vista!5e0!3m2!1sen!2sin!4v1715473561085!5m2!1sen!2sin"',
    'src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d15082.903823483984!2d72.83617651738281!3d19.1634591!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3be7b65389656cd9%3A0x6e9a65d5029bcda!2sRustomjee%20Ozone!5e0!3m2!1sen!2sin!4v1716388480392!5m2!1sen!2sin"'
)

# About builder
old_builder = '''                    <h2 class="font-heading text-3xl md:text-4xl font-bold text-[#C9211A] mb-8">About Mahindra Group
                    </h2>
                    <div class="w-24 h-1 bg-secondary mx-auto mb-8"></div>
                    <p class="text-lg text-gray-600 leading-relaxed mb-8 font-body">
                        Mahindra Lifespaces, the real estate and infrastructure development arm of the Mahindra Group,
                        was established in 1994. With over three decades of experience, the company has built a strong
                        reputation for creating sustainable urban developments across India. Mahindra Lifespaces has
                        successfully delivered residential projects, integrated cities, and industrial clusters, all
                        designed with a focus on eco-friendly construction and customer satisfaction. Their commitment
                        to quality, innovation, and green practices has made them one of the most trusted names in the
                        industry.

                    </p>
                    <div class="grid md:grid-cols-3 gap-8 mt-12">
                        <div class="text-center">
                            <div class="font-secondary text-3xl font-bold text-[#C9211A] mb-2">72MN SQ.FT.</div>
                            <p class="text-gray-800">Under Development and Planning Stages</p>
                        </div>
                        <div class="text-center">
                            <div class="font-secondary text-3xl font-bold text-[#C9211A] mb-2">9,600
                                +</div>
                            <p class="text-gray-800">Homes delivered</p>
                        </div>
                        <div class="text-center">
                            <div class="font-secondary text-3xl font-bold text-[#C9211A] mb-2">43M+</div>
                            <p class="text-gray-800">Sq.ft Developed</p>
                        </div>
                    </div>'''

new_builder = '''                    <h2 class="font-heading text-3xl md:text-4xl font-bold text-[#C9211A] mb-8">About NeoLiv Group
                    </h2>
                    <div class="w-24 h-1 bg-secondary mx-auto mb-8"></div>
                    <p class="text-lg text-gray-600 leading-relaxed mb-8 font-body">
                        NeoLiv Group is a premier, integrated residential real estate platform founded in 2023 with a vision to revolutionize the living experience in India. Led by Mohit Malhotra, the former MD & CEO of Godrej Properties, and a team of seasoned industry professionals, the group brings decades of elite expertise to the forefront of urban development. Built on the pillars of transparency, customer-centricity, and timely delivery, NeoLiv focuses on high-growth corridors across the Delhi-NCR and the Mumbai Metropolitan Region (MMR).
                        <br><br>
                        By combining institutional capital with a deep understanding of modern lifestyle needs, NeoLiv creates "standard-led" developments. For the new phase of Rustomjee Ozone, the group’s unique equity-linked model ensures a high level of accountability and execution trust, making them the preferred choice for modern homeowners and investors looking for premium quality and future-ready spaces.
                    </p>'''

content = content.replace(old_builder, new_builder)

# Footer
content = content.replace(
    'Mahindra Vista Kandivali East is a premium residential project by Mahindra Lifespaces,\n                                offering luxurious 2, 3 & 4 BHK residences with a blend of luxury and nature.',
    'Rustomjee Ozone Goregaon West is a premium high-rise G+49 tower by NeoLiv Group,\n                                offering highly efficient 2 & 3 BHK premium residences at SV Road.'
)
content = content.replace(
    '<strong>Possession:</strong> December 2028 *',
    '<strong>RERA No:</strong> Coming Soon'
)
content = content.replace(
    '© 2025 Mahindra Vista Kandivali East. All rights reserved.',
    '© 2026 Rustomjee Ozone (New Phase). All rights reserved.'
)
content = content.replace(
    'MAHA RERA Project Registration No.: P51800054671',
    'MAHA RERA Project Registration No.: Coming Soon'
)
content = content.replace(
    '<span>Off Western Express Highway, Akurli Road, Kandivali East</span>',
    '<span>SV Road, Mahesh Nagar, Goregaon West, Mumbai</span>'
)

# And Rustomjee Ozone logo alt text
content = content.replace('alt="Mahindra logo"', 'alt="Rustomjee Ozone logo"')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
