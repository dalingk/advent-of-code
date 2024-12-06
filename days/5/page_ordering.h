#ifndef PAGE_ORDERING
#define PAGE_ORDERING
#include <istream>
#include <map>
#include <tuple>
#include <unordered_set>
#include <vector>

#define LINE_SIZE 1024

typedef std::map<int, std::unordered_set<int>> PageOrderings;
typedef PageOrderings ReversedPageOrderings;
typedef std::vector<int> PageUpdate;
typedef std::vector<PageUpdate> PageUpdates;

std::tuple<PageOrderings, PageUpdates>
load_file(std::istream&);

bool
is_valid_page_update(const PageUpdate&, const PageOrderings&);

PageUpdate
correct_update(const PageUpdate&, const PageOrderings&);

#endif // PAGE_ORDERING