# cpp.json

[TOC]

## ショートカット系

<details>
<summary>10digits (digset)	小数の表示桁数を設定</summary>

```10digits.cpp
cout << fixed << setprecision(20);
```
</details>

<details>
<summary>chmin (chmin)</summary>

```chmin.cpp
$1 = min($1, $2);
```
</details>

<details>
<summary>chmax (chmax)</summary>

```chmax.cpp
$1 = max($1, $2);
```
</details>

<details>
<summary>scanf1 (sf1)</summary>

```scanf1.cpp
scanf("%$1", &$2);
```
</details>

<details>
<summary>printf1 (pf1)</summary>

```printf1.cpp
printf("%$1\n", $2);
```
</details>

<details>
<summary>scanf2 (sf2)</summary>

```scanf2.cpp
scanf("%$1%$1", &$2, &$3);
```
</details>

<details>
<summary>printf2 (pf2)</summary>

```printf2.cpp
printf("%$1 %$1\n", $2, $3);
```
</details>

<details>
<summary>scanf3 (sf3)</summary>

```scanf3.cpp
scanf("%$1%$1%$1", &$2, &$3, &$4);
```
</details>

<details>
<summary>printf3 (pf3)</summary>

```printf3.cpp
printf("%$1 %$1 %$1\n", $2, $3, $4);
```
</details>

<details>
<summary>scanf4 (sf4)</summary>

```scanf4.cpp
scanf("%$1%$1%$1%$1", &$2, &$3, &$4, &$5);
```
</details>

<details>
<summary>printf4 (pf4)</summary>

```printf4.cpp
printf("%$1 %$1 %$1 %$1\n", $2, $3, $4, $5);
```
</details>

<details>
<summary>sedge (sedge)</summary>

```sedge.cpp
struct edge {
    int to, cost;
    edge(int to, int cost) : to(to), cost(cost) {}
};
```
</details>

<details>
<summary>ssedge (ssedge)</summary>

```ssedge.cpp
struct edge {
    int to;
    edge(int to) : to(to) {}
};
```
</details>

<details>
<summary>graph (graph)</summary>

```graph.cpp
vector<vector<edge>> G$1;
```
</details>

<details>
<summary>pll (pll)</summary>

```pll.cpp
using P = pair<ll, ll>;
```
</details>

<details>
<summary>pint (pint)</summary>

```pint.cpp
using P = pair<int, int>;
```
</details>

<details>
<summary>vecp (vecp)</summary>

```vecp.cpp
vector<P> $1;
```
</details>

<details>
<summary>vint (vint)</summary>

```vint.cpp
vector<int>
```
</details>

<details>
<summary>vvint (vvint)</summary>

```vvint.cpp
vector<vector<int>> $1 = vector<vector<int>>($2, vector<int>($3));
```
</details>

<details>
<summary>vvvint (vvvint)</summary>

```vvvint.cpp
vector<vector<vector<int>>> $1 = vector<vector<vector<int>>>($2, vector<vector<int>>($3, vector<int>($4)));
```
</details>

<details>
<summary>vmint (vmint)</summary>

```vmint.cpp
vector<mint>
```
</details>

<details>
<summary>vvmint (vvmint)</summary>

```vvmint.cpp
vector<vector<mint>> $1 = vector<vector<mint>>($2, vector<mint>($3));
```
</details>

<details>
<summary>vvvmint (vvvmint)</summary>

```vvvmint.cpp
vector<vector<vector<mint>>> $1 = vector<vector<vector<mint>>>($2, vector<vector<mint>>($3, vector<mint>($4)));
```
</details>

<details>
<summary>vll (vll)</summary>

```vll.cpp
vector<ll>
```
</details>

<details>
<summary>vvll (vvll)</summary>

```vvll.cpp
vector<vector<ll>> $1 = vector<vector<ll>>($2, vector<ll>($3));
```
</details>

<details>
<summary>vvvll (vvvll)</summary>

```vvvll.cpp
vector<vector<vector<ll>>> $1 = vector<vector<vector<ll>>>($2, vector<vector<ll>>($3, vector<ll>($4)));
```
</details>

<details>
<summary>vbool (vbool)</summary>

```vbool.cpp
vector<bool>
```
</details>

<details>
<summary>vvbool (vvbool)</summary>

```vvbool.cpp
vector<vector<bool>> $1 = vector<vector<bool>>($2, vector<bool>($3));
```
</details>

<details>
<summary>vvvbool (vvvbool)</summary>

```vvvbool.cpp
vector<vector<vector<bool>>> $1 = vector<vector<vector<bool>>>($2, vector<vector<bool>>($3, vector<bool>($4)));
```
</details>

<details>
<summary>ca (ca)</summary>

```ca.cpp
const auto 
```
</details>

<details>
<summary>caref (caref)</summary>

```caref.cpp
const auto &
```
</details>

<details>
<summary>debug0 (db0)</summary>

```debug0.cpp
cerr << endl;
```
</details>

<details>
<summary>debug1 (db1)</summary>

```debug1.cpp
cerr << $1 << endl;
```
</details>

<details>
<summary>debug2 (db2)</summary>

```debug2.cpp
cerr << $1 << " " << $2 << endl;
```
</details>

<details>
<summary>debug3 (db3)</summary>

```debug3.cpp
cerr << $1 << " " << $2 << " " << $3 << endl;
```
</details>

<details>
<summary>debug4 (db4)</summary>

```debug4.cpp
cerr << $1 << " " << $2 << " " << $3 << " " << $4 << endl;
```
</details>

<details>
<summary>cout0 (ct0)</summary>

```cout0.cpp
cout << "\n";
```
</details>

<details>
<summary>cout1 (ct1)</summary>

```cout1.cpp
cout << $1 << "\n";
```
</details>

<details>
<summary>cout2 (ct2)</summary>

```cout2.cpp
cout << $1 << " " << $2 << "\n";
```
</details>

<details>
<summary>cout3 (ct3)</summary>

```cout3.cpp
cout << $1 << " " << $2 << " " << $3 << "\n";
```
</details>

<details>
<summary>cout4 (ct4)</summary>

```cout4.cpp
cout << $1 << " " << $2 << " " << $3 << " " << $4 << "\n";
```
</details>

<details>
<summary>cin1 (cn1)</summary>

```cin1.cpp
cin >> $1;
```
</details>

<details>
<summary>cin2 (cn2)</summary>

```cin2.cpp
cin >> $1 >> $2;
```
</details>

<details>
<summary>cin3 (cn3)</summary>

```cin3.cpp
cin >> $1 >> $2 >> $3;
```
</details>

<details>
<summary>cin4 (cn4)</summary>

```cin4.cpp
cin >> $1 >> $2 >> $3 >> $4;
```
</details>

<details>
<summary>cin5 (cn5)</summary>

```cin5.cpp
cin >> $1 >> $2 >> $3 >> $4 >> $5;
```
</details>

<details>
<summary>fastio (fastio)	cinを高速に</summary>

```fastio.cpp
ios_base::sync_with_stdio(false);
cin.tie(NULL);
```
</details>

<details>
<summary>pqrev (pqrev)	逆順のpriority_queue</summary>

```pqrev.cpp
priority_queue<P, vector<P>, greater<P>> 
```
</details>

<details>
<summary>loop4dir (loop4dir)</summary>

```loop4dir.cpp
            rep(i, 4) {
                int ny = y + dy[i], nx = x + dx[i];
                if (ny < 0 || ny >= h || nx < 0 || nx >= w)
                    continue;
            }
```
</details>

<details>
<summary>func (func)</summary>

```func.cpp
[&]($2) -> ${3:int} {$0};
```
</details>

<details>
<summary>iolll (iolll)	int128の</summary>

```iolll.cpp
inline ostream& operator<<(ostream& os, lll val) noexcept {
    string s;
    bool neg = val < 0;
    if (val < 0) {
        val *= -1;
    }
    if (val == 0) {
        s += '0';
    } else {
        while (val > 0) {
            s += '0' + val % 10;
            val /= 10;
        }
    }
    reverse(all(s));
    if (neg) s = "-" + s;
    return os << s;
}
inline istream& operator>>(istream& is, lll& val) noexcept {
    string s;
    is >> s;
    bool neg = false;
    if (s[0] == '-') {
        neg = true;
        s = s.substr(1);
    }
    val = 0;
    for (auto c : s) {
        val *= 10;
        val += c - '0';
    }
    if (neg) val *= -1;
    return is;
}
```
</details>

<details>
<summary>find_SG (find_SG)	グリッドのスタート，ゴール地点を見つける</summary>

```find_SG.cpp
auto find_SG = [](const auto& v) -> tuple<int, int, int, int> {
    const int h = v.size(), w = v.at(0).size();
    int sy = -1, sx = -1, gy = -1, gx = -1;
    rep(i, h) rep(j, w) {
        if (v[i][j] == 'S' || v[i][j] == 's') {
            sy = i;
            sx = j;
        } else if (v[i][j] == 'G' || v[i][j] == 'g') {
            gy = i;
            gx = j;
        }
    }
    assert(sy != -1 && sx != -1 && gy != -1 && gx != -1);
    return {sy, sx, gy, gx};
};
```
</details>

<details>
<summary>to_vint (to_vint)</summary>

```to_vint.cpp
vector<ll> to_vint(ll x, ll base = 10, bool string_ord = false) {
    vector<ll> res;
    while (x) {
        res.push_back(x % base);
        x /= base;
    }
    if (string_ord) reverse(all(res));
    return res;
}
```
</details>

<details>
<summary>myrandom (myrandom)</summary>

```myrandom.cpp
class Random {
   public:
    mt19937 mt;
    mt19937_64 mt64;
    Random() {
        random_device rd;
        mt = mt19937(rd());
        mt64 = mt19937_64(rd());
    }

    int randRange(int l, int r) {
        uniform_int_distribution<int> dist(l, r - 1);
        return dist(mt);
    }
    ll randRangell(ll l, ll r) {
        uniform_int_distribution<ll> dist(l, r - 1);
        return dist(mt64);
    }
    pair<int, int> randPairDistinct(int l, int r) {
        int x = l, y = l;
        do {
            x = randRange(l, r), y = randRange(l, r);
        } while (x == y);
        return {x, y};
    }
    pair<ll, ll> randPairDistinct(ll l, ll r) {
        ll x = l, y = l;
        do {
            x = randRangell(l, r), y = randRangell(l, r);
        } while (x == y);
        return {x, y};
    }
    vector<int> randPerm(int n, int start = 0) {
        vector<int> res(n);
        iota(res.begin(), res.end(), start);
        shuffle(res.begin(), res.end(), mt);
        return res;
    }
    vector<int> randArray(int n, int l, int r) {
        vector<int> res(n);
        uniform_int_distribution<int> dist(l, r - 1);
        for (int i = 0; i < n; i++) res[i] = dist(mt);
        return res;
    }
    vector<ll> randArrayll(int n, ll l, ll r) {
        vector<ll> res(n);
        uniform_int_distribution<ll> dist(l, r - 1);
        for (int i = 0; i < n; i++) res[i] = dist(mt64);
        return res;
    }
    vector<int> randArrayDistinct(int n, int l, int r) {
        assert(r - l >= n);
        vector<int> res(n);
        uniform_int_distribution<int> dist(l, r - 1);
        set<int> st;
        while (st.size() < n) st.insert(dist(mt));
        copy(st.begin(), st.end(), res.begin());
        shuffle(res.begin(), res.end(), mt);
        return res;
    }
    vector<ll> randArrayDistinctll(int n, ll l, ll r) {
        assert(r - l >= n);
        vector<ll> res(n);
        uniform_int_distribution<ll> dist(l, r - 1);
        set<ll> st;
        while (st.size() < n) st.insert(dist(mt64));
        copy(st.begin(), st.end(), res.begin());
        shuffle(res.begin(), res.end(), mt);
        return res;
    }
    vector<pair<int, int>> randTree(int n) {
        assert(n >= 2);
        vector<int> prufer = randArray(n - 2, 0, n);
        return prufer_sequence_to_tree(prufer);
    }
    vector<pair<int, int>> prufer_sequence_to_tree(const vector<int>& a) {
        const int n = a.size() + 2;
        vector<int> deg(n, 1);
        for (int x : a) {
            assert(0 <= x && x < n);
            deg[x]++;
        }
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int i = 0; i < n; ++i)
            if (deg[i] == 1) pq.push(i);
        vector<pair<int, int>> res;
        for (int v : a) {
            int u = pq.top();
            pq.pop();
            res.emplace_back(min(v, u), max(v, u));
            --deg[u], --deg[v];
            if (deg[v] == 1) pq.push(v);
        }
        int x = pq.top();
        pq.pop();
        int y = pq.top();
        res.emplace_back(min(x, y), max(x, y));
        return res;
    }
    vector<pair<int, int>> randGraphConnectedUD(int n, int m) {
        assert(m >= n - 1);
        assert(ll(n) * (n - 1) / 2 >= m);
        vector<pair<int, int>> res = randTree(n);
        set<pair<int, int>> edgesSt;
        for (auto e : res) edgesSt.insert(e);
        if (n <= 1000) {
            vector<pair<int, int>> edges;
            for (int i = 0; i < n - 1; ++i)
                for (int j = i + 1; j < n; ++j)
                    if (!edgesSt.contains({i, j})) edges.emplace_back(i, j);
            shuffle(edges.begin(), edges.end(), mt);
            assert(edges.size() >= m - n + 1);
            for (int i = 0; i < m - n + 1; ++i) res.emplace_back(edges[i]);
        } else {
            while (res.size() < m) {
                auto [x, y] = randPairDistinct(0, n);
                if (x > y) swap(x, y);
                if (!edgesSt.contains({x, y})) {
                    res.emplace_back(x, y);
                    edgesSt.insert({x, y});
                }
            }
        }
        return res;
    }
    inline static string LOWER = "abcdefghijklmnopqrstuvwxyz";
    inline static string UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    inline static string DIGIT = "0123456789";
    inline static string ALPHABET = LOWER + UPPER;
    string randString(int n, string chars = LOWER) {
        string res(n, ' ');
        uniform_int_distribution<int> dist(0, chars.size() - 1);
        for (auto&& c : res) c = chars[dist(mt)];
        return res;
    }
};
```
</details>

<details>
<summary>zeroPadding (zeroPadding)</summary>

```zeroPadding.cpp
auto zeroPadding = [&](auto x, int w) -> string {
    stringstream ss;
    ss << setw(w) << setfill('0') << x;
    return ss.str();
};
```
</details>

<details>
<summary>tint (tint)</summary>

```tint.cpp
using T = tuple<int, int, int>;
```
</details>

<details>
<summary>tll (tll)</summary>

```tll.cpp
using T = tuple<ll, ll, ll>;
```
</details>

<details>
<summary>encodedecode (encodedecode)</summary>

```encodedecode.cpp
    auto encode = [](int S, int len, int base) {
        vector<int> v(len);
        for (auto& e : v) e = S % base, S /= base;
        return v;
    };
    auto decode = [](const vector<int>& v, int base) {
        int S = 0;
        for (const auto& e : v | views::reverse) S = S * base + e;
        return S;
    };
```
</details>


## 定数とか

<details>
<summary>dxdy5 (dxdy5)	近傍5マス</summary>

```dxdy5.cpp
const int dx[] = {-1, 0, 0, 0, 1};
const int dy[] = {0, -1, 0, 1, 0};
```
</details>

<details>
<summary>dxdy8 (dxdy8)	近傍8マス</summary>

```dxdy8.cpp
const int dx[] = {-1, -1, -1, 0, 0, 1, 1, 1};
const int dy[] = {-1, 0, 1, -1, 1, -1, 0, 1};
```
</details>

<details>
<summary>dxdy9 (dxdy9)	近傍9マス</summary>

```dxdy9.cpp
const int dx[] = {-1, -1, -1, 0, 0, 0, 1, 1, 1};
const int dy[] = {-1, 0, 1, -1, 0, 1, -1, 0, 1};
```
</details>

<details>
<summary>dxdy4 (dxdy4)	近傍4マス,反時計回り</summary>

```dxdy4.cpp
const int dx[] = {1, 0, -1, 0};
const int dy[] = {0, 1, 0, -1};
```
</details>


## 簡単な関数

<details>
<summary>degrad (degrad)	deg,rad変換</summary>

```degrad.cpp
double d2r(double deg) { return deg / 360 * 2 * M_PI; }
double r2d(double rad) { return rad / 2 / M_PI * 360; }
```
</details>


## テンプレ

<details>
<summary>cftenpure (cftenpure)	Codeforcesのテンプレ</summary>

```cftenpure.cpp
#include <bits/stdc++.h>

using ll = long long;
#define rep(i, n) for (int i = 0, i##_len = (n); i < i##_len; ++i)
#define reps(i, n) for (int i = 1, i##_len = (n); i <= i##_len; ++i)
#define rrep(i, n) for (int i = ((int)(n)-1); i >= 0; --i)
#define rreps(i, n) for (int i = ((int)(n)); i > 0; --i)
#define rep2(i, s, n) for (int i = (s); i < (int)(n); i++)
#define repc2(i, s, n) for (int i = (s); i <= (int)(n); i++)
#define bitrep(i, n) for (int i = 0, i##_len = (1 << (int)(n)); i < i##_len; i++)
#define bitrrep(i, n) for (int i = (1 << (int)(n)) - 1ll; i >= 0; i--)
constexpr int inf = 2000'000'000;
constexpr ll linf = 4000000000000000000ll;
constexpr ll M7 = 1000000007ll;
constexpr ll M09 = 1000000009ll;
constexpr ll M9 = 998244353ll;
#define all(v) begin(v), end(v)
#define rall(v) rbegin(v), rend(v)
using namespace std;
template <typename T>
inline ostream& operator<<(ostream& os, vector<T>& v) {
    for (auto& e : v) os << e << " ";
    return os;
}
template <typename T, typename U>
std::ostream& operator<<(std::ostream& os, const std::pair<T, U>& p) noexcept {
    return os << "(" << p.first << ", " << p.second << ")";
}

ll Q;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> Q;
    rep(_i, Q) {
        ll n;
        cin >> n;
    }
    return 0;
}
```
</details>

<details>
<summary>procon (procon)</summary>

```procon.cpp
#include <bits/stdc++.h>
using ll = long long;
#define rep(i, n) for (int i = 0, i##_len = (n); i < i##_len; ++i)
#define reps(i, n) for (int i = 1, i##_len = (n); i <= i##_len; ++i)
#define rrep(i, n) for (int i = ((int)(n)-1); i >= 0; --i)
#define rreps(i, n) for (int i = ((int)(n)); i > 0; --i)
#define rep2(i, s, n) for (int i = (s); i < (int)(n); i++)
#define repc2(i, s, n) for (int i = (s); i <= (int)(n); i++)
constexpr int inf = 2000'000'000;
constexpr ll linf = 4000000000000000000ll;
constexpr ll M7 = 1000000007ll;
constexpr ll M09 = 1000000009ll;
constexpr ll M9 = 998244353ll;
#define all(v) begin(v), end(v)
#define rall(v) rbegin(v), rend(v)
using namespace std;
template <typename T>
inline ostream& operator<<(ostream& os, const vector<T>& v) {
    for (auto itr = v.begin(); itr != v.end(); ++itr) {
        os << *itr;
        if (itr != v.end() - 1) {
            os << " ";
        }
    }
    return os;
}
template <typename T, typename U>
std::ostream& operator<<(std::ostream& os, const std::pair<T, U>& p) noexcept {
    return os << "(" << p.first << ", " << p.second << ")";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    return 0;
}
```
</details>

<details>
<summary>oldatcd (oldatcd)	旧ジャッジ</summary>

```oldatcd.cpp
#include <bits/stdc++.h>

#include <atcoder/all>
using ll = long long;
using lll = __int128_t;
#define rep(i, n) for (int i = 0, i##_len = (n); i < i##_len; ++i)
#define reps(i, n) for (int i = 1, i##_len = (n); i <= i##_len; ++i)
#define rrep(i, n) for (int i = ((int)(n)-1); i >= 0; --i)
#define rreps(i, n) for (int i = ((int)(n)); i > 0; --i)
#define rep2(i, s, n) for (int i = (s); i < (int)(n); i++)
#define repc2(i, s, n) for (int i = (s); i <= (int)(n); i++)
constexpr int inf = 2000'000'000;
constexpr ll linf = 4'000'000'000'000'000'000ll, M7 = 1'000'000'007ll, M9 = 998'244'353ll;
#define all(v) begin(v), end(v)
#define rall(v) rbegin(v), rend(v)
using namespace std;
using namespace atcoder;

template <typename T, typename U>
inline ostream& operator<<(ostream& os, const pair<T, U>& p) noexcept {
    return os << p.first << " " << p.second;
}

inline ostream& operator<<(ostream& os, const modint998244353& m) noexcept { return os << m.val(); }
inline ostream& operator<<(ostream& os, const modint1000000007& m) noexcept { return os << m.val(); }
inline ostream& operator<<(ostream& os, const modint& m) noexcept { return os << m.val(); }

inline string YESNO(bool cond) { return cond ? "YES" : "NO"; }
inline string yesno(bool cond) { return cond ? "yes" : "no"; }
inline string YesNo(bool cond) { return cond ? "Yes" : "No"; }
inline auto add1(const auto& vec) {
    auto res = vec;
    for (auto&& e : res) ++e;
    return res;
}
#ifdef ONLINE_JUDGE
#define debug(...)
#else
#define debug(...) cerr << "<" << #__VA_ARGS__ << ">: ", debug_out(__VA_ARGS__)
template <typename T>
void debug_out(T t) {
    cerr << t << endl;
}
template <typename T, typename... Args>
void debug_out(T t, Args... args) {
    cerr << t << ", ";
    debug_out(args...);
}
#endif

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    return 0;
}
```
</details>

<details>
<summary>atcdm (atcdm)	AtCoderのテンプレ</summary>

```atcdm.cpp
#ifdef ONLINE_JUDGE
#include <bits/stdc++.h>

#include <atcoder/all>
#else
#include <mylibs/all.h>
#endif

using ll = long long;
using lll = __int128_t;
#define rep(i, n) for (int i = 0, i##_len = (n); i < i##_len; ++i)
#define reps(i, n) for (int i = 1, i##_len = (n); i <= i##_len; ++i)
#define rrep(i, n) for (int i = ((int)(n)-1); i >= 0; --i)
#define rreps(i, n) for (int i = ((int)(n)); i > 0; --i)
#define rep2(i, s, n) for (int i = (s); i < (int)(n); i++)
#define repc2(i, s, n) for (int i = (s); i <= (int)(n); i++)
#define length(v) ((int)(v).size())
constexpr int inf = 2'000'000'000;
constexpr ll linf = 4'000'000'000'000'000'000, M7 = 1'000'000'007, M9 = 998'244'353;
#define all(v) begin(v), end(v)
#define rall(v) rbegin(v), rend(v)
using namespace std;
using namespace atcoder;

// clang-format off
#define Vec(type, ...) __make_vec<type>(__VA_ARGS__)
template <class T> vector<T> __make_vec(size_t a) {return vector<T>(a);}template <class T, class... Ts>
auto __make_vec(size_t a, Ts... ts) {return vector<decltype(__make_vec<T>(ts...))>(a, __make_vec<T>(ts...));}
#define VecI(init, type, ...) __make_vecI<type, init>(__VA_ARGS__)
template <class T, T init>vector<T> __make_vecI(size_t a) {return vector<T>(a, init);}
template <class T, T init, class... Ts>
auto __make_vecI(size_t a, Ts... ts) {return vector<decltype(__make_vecI<T, init>(ts...))>(a, __make_vecI<T, init>(ts...));}

template <typename T, typename U>inline ostream& operator<<(ostream& os, const pair<T, U>& p) noexcept {return os << p.first << " " << p.second;}
inline ostream& operator<<(ostream& os, const modint& m) noexcept { return os << m.val(); }
template <int M>inline ostream& operator<<(ostream& os, const static_modint<M>& m) noexcept { return os << m.val(); }

template <typename T> struct is_static_modint : std::false_type {}; template <int MOD> struct is_static_modint<static_modint<MOD>> : std::true_type {};
template <template <typename...> typename C, typename Number>concept MyContainer = std::is_same_v<C<Number>, std::vector<Number>> || std::is_same_v<C<Number>, std::deque<Number>> || std::is_same_v<C<Number>, std::set<Number>> || std::is_same_v<C<Number>, std::unordered_set<Number>> || std::is_same_v<C<Number>, std::unordered_multiset<Number>> || std::is_same_v<C<Number>, std::multiset<Number>>;
template <typename Number>concept MyNumber = std::is_same_v<Number, int> || std::is_same_v<Number, ll> || std::is_same_v<Number, char> || std::is_same_v<Number, modint> || is_static_modint<Number>::value;
template <template <typename...> typename C, typename Number>concept MyContainerNumber = MyContainer<C, Number> && MyNumber<Number>;
template <template <typename...> typename OutCon, template <typename...> typename InCon, typename Number>concept MyNestedContainerNumber = MyContainer<OutCon, InCon<Number>> && MyContainerNumber<InCon, Number>;
template <template <typename...> typename C, typename Number>requires MyContainerNumber<C, Number>std::ostream& operator<<(std::ostream& os, const C<Number>& t) {auto itr = t.begin();auto end = t.end();if (itr != end) {os << *itr++;for (; itr != end; ++itr) os << ' ' << *itr;}return os;}
template <template <typename...> typename OutCon, template <typename...> typename InCon, typename Number>requires MyNestedContainerNumber<OutCon, InCon, Number>std::ostream& operator<<(std::ostream& os, const OutCon<InCon<Number>>& t) {auto itr = t.begin();auto end = t.end();if (itr != end) {os << *itr++;for (; itr != end; ++itr) os << '\n' << *itr;}return os;}
template <typename T, typename U>istream& operator>>(istream& is, pair<T, U>& p) {return is >> p.first >> p.second;}
template <typename T>istream& operator>>(istream& is, vector<T>& v) {for (auto& e : v) is >> e;return is;}
void inp() {}
template <typename T, typename... Args>void inp(T& a, Args&... args) {cin >> a, inp(args...);}
template <typename T>void inp1(vector<T>& v, int offset = 1, int len = -1) {if (len == -1) len = int(v.size()) - offset;assert(offset >= 0 && len >= 0);for (int i = offset; i < offset + len; ++i) cin >> v[i];}
template <typename T>void oup(const T& a) {cout << a << "\n";}
template <typename T, typename... Args>void oup(const T& a, const Args&... args) {cout << a << " ", oup(args...);}

inline string YESNO(bool cond) { return cond ? "YES" : "NO"; }inline string yesno(bool cond) { return cond ? "yes" : "no"; }inline string YesNo(bool cond) { return cond ? "Yes" : "No"; }
inline auto add1(auto vec, ll offset = 1) {for (auto& e : vec) e += offset;return vec;}
#ifdef ONLINE_JUDGE
#define debug(...)
#else
#define debug(...) cerr << "<" << #__VA_ARGS__ << ">: ", debug_out(__VA_ARGS__)
template <typename T>void debug_out(T t) {cerr << t << "\n";}
template <typename T, typename... Args>void debug_out(T t, Args... args) {cerr << t << ", ";debug_out(args...);}
#endif
// clang-format on


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);$0
    return 0;
}
```
</details>


## アルゴリズム，データ構造

### 未分類

<details>
<summary>inversion (inversion)	転倒数</summary>

```inversion.cpp
auto inversion = [](const auto& v) {
    const int n = v.size();
    fenwick_tree<int> bit(n);
    vector<int> idx(n);
    iota(all(idx), 0);
    sort(all(idx), [&](int i, int j) { return v[i] == v[j] ? i > j : v[i] > v[j]; });
    long long ans = 0;
    for (auto&& id : idx) {
        ans += bit.sum(0, id);
        bit.add(id, 1);
    }
    return ans;
};
```
</details>

<details>
<summary>bSearchF (bSearchF)</summary>

```bSearchF.cpp
auto bsearchF = [&](bool check = true) {
    double ok = $1, ng = $2;
    if (check) assert(cmp(ok) && !cmp(ng));
    rep(i, 100) {
        double mid = (ng + ok) / 2;
        if (cmp(mid)) ok = mid;
        else ng = mid;
    }
    return ok;
};
```
</details>

<details>
<summary>binCount (binCount)</summary>

```binCount.cpp
auto binCount = [&](const auto& v, int maxNum = -1) {
    if (maxNum < 0) maxNum = *max_element(all(v));
    vector<ll> cnt(maxNum + 1);
    for (const auto& e : v) cnt.at(e)++;
    return cnt;
};
```
</details>

<details>
<summary>myrange (myrange)	区間クラス</summary>

```myrange.cpp
struct MyRange {
    ll l, r;
    MyRange(ll l, ll r) : l(l), r(r) {
        if (l > r) l = r = 0ll;
    }
    MyRange() : MyRange(0ll, 0ll) {}
    MyRange operator&(MyRange b) const {
        ll nl = max(l, b.l), nr = min(r, b.r);
        if (nl < nr) return MyRange(nl, nr);
        else return MyRange();
    }
    MyRange operator|(MyRange b) const {  // 1つの区間になる時のみ繋げる
        if (max(l, b.l) > min(r, b.r)) return MyRange();
        return MyRange(min(l, b.l), max(r, b.r));
    }
    bool empty() const { return l == r; }
    bool contain(ll x) const { return l <= x && x < r; }
    ll count() const { return r - l; }
};
```
</details>


### 数学系

<details>
<summary>Isprime (Isprime)	試し割り</summary>

```Isprime.cpp
bool isPrime(int x) {
    if (x <= 1) return false;
    int sqx = sqrt(x);
    for (int i = 2; i <= sqx; i++) {
        if (x % i == 0) {
            return false;
        }
    }
    return true;
}
```
</details>

<details>
<summary>prime_factorize (prime_factorize)</summary>

```prime_factorize.cpp
vector<int> prime_factorize(int n) {
    if (n <= 1) return {};
    vector<int> ans;
    for (int i = 2; i * i <= n; i++) {
        while (n % i == 0) {
            ans.push_back(i);
            n /= i;
        }
    }
    if (n != 1) {
        ans.push_back(n);
    }
    return ans;
}
```
</details>

<details>
<summary>pchmint (pchmint)	線形時間逆元列挙、階乗、組み合わせのnPr,nCr,nHr</summary>

```pchmint.cpp
constexpr ll MOD = M9;
using mint = static_modint<MOD>;
struct modInv {
    int n;
    vector<mint> d;
    modInv() : n(2), d({0, 1}) {}
    mint operator()(int i) {
        while (n <= i) d.emplace_back(-d[MOD % n] * (MOD / n)), ++n;
        return d[i];
    }
    mint operator[](int i) const { return d[i]; }
} invs;
struct Factorial {
    int n;
    vector<mint> d;
    Factorial() : n(2), d({1, 1}) {}
    mint operator()(int i) {
        while (n <= i) d.emplace_back(d.back() * n), ++n;
        return d[i];
    }
    mint operator[](int i) const { return d[i]; }
} factorial;
struct FactorialInv {
    int n;
    vector<mint> d;
    FactorialInv() : n(2), d({1, 1}) {}
    mint operator()(int i) {
        while (n <= i) d.emplace_back(d.back() * invs(n)), ++n;
        return d[i];
    }
    mint operator[](int i) const { return d[i]; }
} factorialInv;
mint P(int n, int r) {
    if (n < r || n < 0 || r < 0) return 0;
    return factorial(n) * factorialInv(n - r);
}
mint C(int n, int r) {
    if (n < r || n < 0 || r < 0) return 0;
    return factorial(n) * factorialInv(r) * factorialInv(n - r);
}
mint H(int n, int r) {
    const int _n = n + r - 1;
    if (_n < r || _n < 0 || r < 0) return 0;
    return factorial(_n) * factorialInv(r) * factorialInv(_n - r);
}
```
</details>

<details>
<summary>divisor (divisor)</summary>

```divisor.cpp
vector<ll> divisor(ll n) {
    vector<ll> res;
    for (ll i = 1; i * i <= n; i++) {
        if (n % i == 0) {
            res.push_back(i);
            if (n / i != i)
                res.push_back(n / i);
        }
    }
    sort(res.begin(), res.end());
    return res;
}
```
</details>


### グラフ理論

<details>
<summary>matpow (matpow)	行列累乗に使うやつ</summary>

```matpow.cpp
typedef vector<vector<ll> > Matrix;
typedef vector<ll> vec;

const ll M = 1000'000'007;

Matrix new_matrix(int n) {
    Matrix res(n, vec(n));
    return res;
}
Matrix new_matrix(int n, int m) {
    Matrix res(n, vec(m));
    return res;
}
Matrix operator*(const Matrix &m1, const Matrix &m2) {
    assert(m1.at(0).size() == m2.size());
    size_t n = m1.size();
    size_t m = m2.at(0).size();
    size_t l = m2.size();
    Matrix res(n, vec(m));
    rep(i, n) rep(j, m) rep(k, l) {
        res.at(i).at(j) += m1.at(i).at(k) * m2.at(k).at(j);
        res.at(i).at(j) %= M;
    }
    return res;
}
vec operator*(const Matrix &m, const vec &v) {
    assert(m.at(0).size() == v.size());
    vec res(v.size());
    rep(i, v.size()) rep(j, m.at(0).size()) {
        res.at(i) += m.at(i).at(j) * v.at(j);
        res.at(i) %= M;
    }
    return res;
}
Matrix E(size_t n) {
    Matrix res(n, vec(n));
    rep(i, n) res.at(i).at(i) = 1;
    return res;
}
Matrix pow(const Matrix &a, long long n) {
    Matrix b = a;
    Matrix res = E(a.size());
    while (n > 0) {
        if (n & 1)
            res = res * b;
        b = b * b;
        n >>= 1ll;
    }
    return res;
}
```
</details>

<details>
<summary>bfs (bfs)</summary>

```bfs.cpp
    auto bfs = [&](int ip) {
        queue<int> que;
        vector<ll> d(G.size(), linf);
        d.at(ip) = 0;
        que.push(ip);
        while (!que.empty()) {
            int u = que.front();
            que.pop();
            for (const auto &eg : G.at(u)) {
                if (d.at(eg.to) > d.at(u) + 1) {
                    d.at(eg.to) = d.at(u) + 1;
                    que.push(eg.to);
                }
            }
        }
        return d;
    };
```
</details>

<details>
<summary>dfs (dfs)</summary>

```dfs.cpp
auto dfs = [&](auto dfs, int u) -> $1 {
        seen.at(u) = true;
        for (const auto &e : G.at(u)) {
            if (seen.at(e.to))
                continue;
            dfs(dfs, e.to);
        }
    };
```
</details>

<details>
<summary>dijkstra (dijkstra)</summary>

```dijkstra.cpp
    auto dijkstra = [&](int ip) {
        using P = pair<ll, int>;
        priority_queue<P, vector<P>, greater<P>> pq;
        vector<ll> dist(G.size(), linf);
        dist.at(ip) = 0;
        pq.emplace(0ll, ip);
        while (!pq.empty()) {
            auto u = pq.top();
            auto [curDist, curPos] = u;
            pq.pop();
            if (curDist > dist.at(curPos))
                continue;
            for (const auto &eg : G.at(curPos)) {
                if (dist.at(eg.to) > dist.at(curPos) + eg.cost) {
                    dist.at(eg.to) = dist.at(curPos) + eg.cost;
                    pq.emplace(dist.at(eg.to), eg.to);
                }
            }
        }
        return dist;
    };
```
</details>

<details>
<summary>bfs01 (bfs01)</summary>

```bfs01.cpp
    auto bfs01 = [&](int ip) {
        using P = pair<int, int>;
        vector<int> d(G.size(), inf);
        deque<int> dq;
        d.at(ip) = 0;
        dq.push_front(ip);
        while (!dq.empty()) {
            auto u = dq.front();
            dq.pop_front();
            for (const auto &eg : G.at(u)) {
                if (d.at(eg.to) > d.at(u) + eg.cost) {
                    d.at(eg.to) = d.at(u) + eg.cost;
                    if (eg.cost == 1)
                        dq.push_back(eg.to);
                    else
                        dq.push_front(eg.to);
                }
            }
        }
        return d;
    };
```
</details>

<details>
<summary>rerooting (rerooting)</summary>

```rerooting.cpp
template <typename T, typename EDGE, T (*merge)(T, T), T (*add)(T), T (*e)()>
class ReRooting {
   private:
    int n;
    std::vector<vector<EDGE>> G;
    std::vector<vector<T>> dp, dp_left, dp_right;  // G[i][j]より先の部分木の値
    std::vector<int> parent, cid, pid;  // 頂点0を親とする根付き木における頂点vの親，親から見て何番目の子か
    std::vector<int> preOrd;            // 帰りがけ順
    std::vector<T> res;

   public:
    T dfs(int u) {
        T r = e();
        preOrd.push_back(u);
        for (int i = 0; i < G.at(u).size(); i++) {
            const auto &eg = G.at(u).at(i);
            if (eg.to != parent.at(u)) {
                cid.at(eg.to) = i;
                parent.at(eg.to) = u;
                r = merge(r, dfs(eg.to));
            } else {
                pid.at(u) = i;
            }
        }
        r = add(r);
        if (parent.at(u) != -1) {
            dp.at(parent.at(u)).at(cid.at(u)) = r;
        }
        return r;
    }

    ReRooting(const std::vector<std::vector<EDGE>> &G) : G(G), n(int(G.size())) {
        dp.resize(n);
        dp_left.resize(n);
        dp_right.resize(n);
        for (int i = 0; i < n; i++) {
            dp.at(i).resize(G.at(i).size());
            dp_left.at(i).resize(G.at(i).size());
            dp_right.at(i).resize(G.at(i).size());
        }
        parent.resize(n, -1);
        cid.resize(n);
        pid.resize(n);
        res.resize(n);

        dfs(0);

        for (int i = 0; i < n; i++) {
            int u = preOrd.at(i);
            if (parent.at(u) != -1) {
                dp.at(u).at(pid.at(u)) = e();
                if (cid.at(u) - 1 != -1)
                    dp.at(u).at(pid.at(u)) = merge(dp.at(u).at(pid.at(u)), dp_left.at(parent.at(u)).at(cid.at(u) - 1));
                if (cid.at(u) + 1 != G.at(parent.at(u)).size())
                    dp.at(u).at(pid.at(u)) = merge(dp.at(u).at(pid.at(u)), dp_right.at(parent.at(u)).at(cid.at(u) + 1));
                dp.at(u).at(pid.at(u)) = add(dp.at(u).at(pid.at(u)));
            }
            dp_left.at(u).at(0) = dp.at(u).at(0);
            for (int j = 1; j < G.at(u).size(); j++) {
                dp_left.at(u).at(j) = merge(dp.at(u).at(j), dp_left.at(u).at(j - 1));
            }
            dp_right.at(u).at(G.at(u).size() - 1) = dp.at(u).at(G.at(u).size() - 1);
            for (int j = G.at(u).size() - 2; j >= 0; j--) {
                dp_right.at(u).at(j) = merge(dp.at(u).at(j), dp_right.at(u).at(j + 1));
            }
            res.at(u) = add(dp_left.at(u).back());
        }
    }

    T get(int u) { return res.at(u); }
};
```
</details>

<details>
<summary>perm_cycle (perm_cycle)	順列を閉路に分解</summary>

```perm_cycle.cpp
auto perm_cycle = [&](const vector<int> &perm) {
        vector<vector<int>> cycles;
        const int n = perm.size();
        vector<bool> seen(n);
        rep(i, n) {
            if (seen[i])
                continue;
            vector<int> cycle;
            int u = i;
            while (!seen[u]) {
                seen[u] = true;
                cycle.emplace_back(u);
                u = perm[u];
            }
            cycles.emplace_back(cycle);
        }
        return cycles;
    };
```
</details>

<details>
<summary>retrograde_analysis (retrograde_analysis)	後退解析, 0->lose, 1->win, -1->draw</summary>

```retrograde_analysis.cpp
auto retrograde_analysis = [](const auto &revG) {
    const int n = revG.size();
    vector<int> dp(n, -1), outDeg(n);
    queue<int> que;
    rep(i, n) {
        for (const auto &e : revG.at(i)) {
            outDeg.at(e.to)++;
        }
    }
    rep(i, n) {
        if (outDeg.at(i) == 0) {
            dp.at(i) = 0;
            que.push(i);
        }
    }
    while (!que.empty()) {
        int u = que.front();
        que.pop();
        for (const auto &e : revG.at(u)) {
            int nv = e.to;
            if (dp.at(nv) != -1)
                continue;
            outDeg.at(nv)--;
            if (dp.at(u) == 0) {
                dp.at(nv) = 1;
                que.push(nv);
            } else if (dp.at(u) == 1 && outDeg.at(nv) == 0) {
                dp.at(nv) = 0;
                que.push(nv);
            }
        }
    }
    return dp;
};
```
</details>

<details>
<summary>contain_cycle_directed (contain_cycle_directed)</summary>

```contain_cycle_directed.cpp
    auto contain_cycle_directed = [](const auto& G) {
        const int n = G.size();
        vector<int> in(n);
        queue<int> que;
        rep(i, n) for (const auto& e : G[i]) in.at(e.to)++;
        rrep(i, n) if (in[i] == 0) que.push(i);
        vector<int> ts;
        while (!que.empty()) {
            auto u = que.front();
            que.pop();
            ts.push_back(u);
            for (const auto& e : G[u]) {
                in.at(e.to)--;
                if (in.at(e.to) == 0)
                    que.push(e.to);
            }
        }
        return ts.size() != n;
    };
```
</details>

<details>
<summary>gridBfs (gridBfs)</summary>

```gridBfs.cpp
auto grid_bfs = [&](const auto& v, int sy, int sx) {
    const int h = v.size(), w = v.at(0).size();
    const int dd[] = {0, 1, 0, -1, 0};
    using P = pair<int, int>;
    queue<P> que;
    vector dist = vector(h, vector<int>(w, inf));
    dist[sy][sx] = 0;
    que.emplace(sy, sx);
    while (!que.empty()) {
        auto [y, x] = que.front();
        que.pop();
        rep(i, 4) {
            int ny = y + dd[i], nx = x + dd[i + 1];
            if (ny < 0 || ny >= h || nx < 0 || nx >= w)
                continue;
            if (v[ny][nx] == '#')
                continue;
            if (dist[ny][nx] > dist[y][x] + 1) {
                dist[ny][nx] = dist[y][x] + 1;
                que.emplace(ny, nx);
            }
        }
    }
    return dist;
};
```
</details>


### その他便利なやつ

<details>
<summary>bSearch (bSearch)</summary>

```bSearch.cpp
auto bsearch = [&](auto cmp) {
    $1 ok = $2, ng = $3;
    while (abs(ng - ok) > 1) {
        $1 mid = (ng + ok) / 2;
        if (cmp(mid))
            ok = mid;
        else
            ng = mid;
    }
    return ok;
};
```
</details>

<details>
<summary>Union Find Trees (unionfind)	unionfind</summary>

```Union Find Trees.cpp
class DisjointSet {
   private:
    vector<int> rank, parent;

   public:
    DisjointSet() {}
    DisjointSet(int size) {
        rank.resize(size, 0);
        parent.resize(size, 0);
        rep(i, size) { makeSet(i); }
    }
    void makeSet(int x) {
        parent[x] = -1;
        rank[x] = 0;
    }
    bool same(int x, int y) { return findSet(x) == findSet(y); }
    void unite(int x, int y) { link(findSet(x), findSet(y)); }
    void link(int x, int y) {
        if (x == y) {
            return;
        }
        if (rank[x] > rank[y]) {
            parent[x] += parent[y];
            parent[y] = x;
        } else {
            parent[y] += parent[x];
            parent[x] = y;
            if (rank[x] == rank[y]) {
                rank[y]++;
            }
        }
    }
    int findSet(int x) {
        if (parent[x] >= 0) {
            parent[x] = findSet(parent[x]);
            return parent[x];
        }
        return x;
    }
    int size(int x) { return -parent[findSet(x)]; }
};
```
</details>

<details>
<summary>compress (compress)	座圧</summary>

```compress.cpp
template <typename T>
struct compress {
   private:
    vector<T> xs;
    vector<int> dst;
    int n;

   public:
    compress(vector<T> x) : n(x.size()), dst(x.size()) {
        rep(i, n) { xs.push_back(x[i]); }
        sort(all(xs));
        xs.erase(unique(all(xs)), xs.end());
        rep(i, n) { dst[i] = distance(xs.begin(), lower_bound(all(xs), x[i])); }
    }

    T get(int i) { return dst[i]; }
    T to_comp(T raw_x) { return distance(xs.begin(), lower_bound(all(xs), raw_x)); }
    T to_raw(int compressed_x) { return xs[compressed_x]; }
}
```
</details>

<details>
<summary>runLengthEndoding (runLengthEndoding)	連長圧縮</summary>

```runLengthEndoding.cpp
auto RLE = [](const auto& v) {
    assert(!v.empty());
    using T = typename decay<decltype(v.front())>::type;
    vector<pair<T, int>> res;
    for (const auto& e : v) {
        if (res.empty() || res.back().first != e) res.emplace_back(e, 1);
        else res.back().second++;
    }
    return res;
};
```
</details>


### SegTree派生のデータ構造

<details>
<summary>fenwicktree (fenwicktree)	0-indexed, [l, r)</summary>

```fenwicktree.cpp
template <typename T>
struct BIT {
    int n;
    vector<T> data;
    BIT(int n) : n(n), data(n + 1, 0) {}
    BIT() {}
    void add(int i, T x = 1) {
        for (i++; i <= n; i += (i & -i)) data[i] += x;
    }
    T sum(int i) {
        T s(0);
        for (i++; i; i -= (i & -i)) s += data[i];
        return s;
    }
    T sum(int l, int r) { return sum(r - 1) - sum(l - 1); }
    T get(int i) { return sum(i) - sum(i - 1); }

    int lower_bound(T w) {
        if (w <= 0) {
            return 0;
        }
        int x = 0, r = 1;
        while (r < n) r <<= 1;
        for (int len = r; len > 0; len >>= 1) {
            if (x + len <= n && data[x + len] < w) {
                w -= data[x + len];
                x += len;
            }
        }
        return x;
    }
};
```
</details>


## 競プロ効率化用の関数，クラス

<details>
<summary>S2 (S2)	ll2つのペア</summary>

```S2.cpp
struct S2 {
    ll x, y;
    S2() : x(0ll), y(0ll){};
    constexpr S2(ll _x, ll _y) : x(_x), y(_y) {}
    constexpr S2 reduced() const {
        ll g = gcd(x, y);
        return {x / g, y / g};
    }
    constexpr S2 operator+() const { return *this; }
    constexpr S2 operator-() const { return {-x, -y}; }
    constexpr S2 operator+(const S2& rhs) const { return {x + rhs.x, y + rhs.y}; }
    constexpr S2 operator-(const S2& rhs) const { return {x - rhs.x, y - rhs.y}; }
    constexpr S2 operator*(ll s) const { return {x * s, y * s}; }
    constexpr S2 operator/(ll s) const { return {x / s, y / s}; }
    S2& operator+=(const S2& rhs) {
        x += rhs.x, y += rhs.y;
        return *this;
    }
    S2& operator-=(const S2& rhs) {
        x -= rhs.x, y -= rhs.y;
        return *this;
    }
    S2& operator*=(ll s) {
        x *= s, y *= s;
        return *this;
    }
    S2& operator/=(ll s) {
        x /= s, y /= s;
        return *this;
    }
};
inline constexpr S2 operator*(ll s, const S2& v) {
    return {s * v.x, s * v.y};
}
inline ostream& operator<<(ostream& os, S2& s) {
    return os << "(" << s.x << ", " << s.y << ")";
}
inline istream& operator>>(istream& is, S2& s) {
    return is >> s.x >> s.y;
}
```
</details>

<details>
<summary>S3 (S3)	ll3つのタプル</summary>

```S3.cpp
struct S3 {
    ll x, y, z;
    S3() : x(0ll), y(0ll), z(0ll){};
    constexpr S3(ll _x, ll _y, ll _z) : x(_x), y(_y), z(_z) {}
    S3 reduced() const {
        ll g = gcd(gcd(x, y), z);
        return {x / g, y / g, z / g};
    }
    constexpr S3 operator+() const { return *this; }
    constexpr S3 operator-() const { return {-x, -y, -z}; }
    constexpr S3 operator+(const S3& rhs) const { return {x + rhs.x, y + rhs.y, z + rhs.z}; }
    constexpr S3 operator-(const S3& rhs) const { return {x - rhs.x, y - rhs.y, z - rhs.z}; }
    constexpr S3 operator*(ll s) const { return {x * s, y * s, z * s}; }
    constexpr S3 operator/(ll s) const { return {x / s, y / s, z / s}; }
    S3& operator+=(const S3& rhs) {
        x += rhs.x, y += rhs.y, z += rhs.z;
        return *this;
    }
    S3& operator-=(const S3& rhs) {
        x -= rhs.x, y -= rhs.y, z -= rhs.z;
        return *this;
    }
    S3& operator*=(ll s) {
        x *= s, y *= s, z *= s;
        return *this;
    }
    S3& operator/=(ll s) {
        x /= s, y /= s, z /= s;
        return *this;
    }
};
inline constexpr S3 operator*(ll s, const S3& v) {
    return {s * v.x, s * v.y, s * v.z};
}
inline ostream& operator<<(ostream& os, S3& s) {
    return os << "(" << s.x << ", " << s.y << ", " << s.z << ")";
}
inline istream& operator>>(istream& is, S3& s) {
    return is >> s.x >> s.y >> s.z;
}
```
</details>


