#include <iostream>
#include <iterator>
#include <sstream>

#include "page_ordering.h"

std::tuple<PageOrderings, PageUpdates>
load_file(std::istream& input_stream)
{
    char line[1024];
    PageOrderings orders;
    PageUpdates updates;

    int tmp_before, tmp_after;
    char tmp_chr;
    std::vector<int> tmp_updates;

    while (input_stream.getline(line, LINE_SIZE)) {
        std::string line_string(line);
        std::istringstream line_stream(line);
        if (line_string.find('|') != std::string::npos) {
            line_stream >> tmp_before >> tmp_chr >> tmp_after;
            orders[tmp_before].insert(tmp_after);
        } else if (line_string.find(',') != std::string::npos) {
            do {
                line_stream >> tmp_before >> tmp_chr;
                tmp_updates.push_back(tmp_before);
            } while (line_stream.good());
            updates.push_back(tmp_updates);
            tmp_updates.clear();
        }
    }

    return std::tuple(orders, updates);
}

bool
is_valid_page_update(const PageUpdate& update, const PageOrderings& orderings)
{
    for (auto update_iterator = update.begin(); update_iterator != update.end(); ++update_iterator) {
        if (orderings.count(*update_iterator) == 0) {
            continue;
        }
        auto before_rules = orderings.find(*update_iterator)->second;
        for (auto order_iterator = update.begin(); order_iterator != update_iterator; ++order_iterator) {
            if (before_rules.count(*order_iterator) > 0) {
                return false;
            }
        }
    }
    return true;
}

PageUpdate
correct_update(const PageUpdate& update, const PageOrderings& orderings)
{
    PageUpdate corrected = update;
    for (auto update_iterator = corrected.begin(); update_iterator != corrected.end(); ++update_iterator) {
        if (orderings.count(*update_iterator) == 0) {
            continue;
        }
        auto before_rules = orderings.find(*update_iterator)->second;
        PageUpdate::iterator target = update_iterator;
        // Inefficient but I have a lot of computer under this desk.
        for (auto order_iterator = update_iterator - 1; order_iterator >= corrected.begin(); --order_iterator) {
            if (before_rules.count(*order_iterator) > 0) {
                target = order_iterator;
            }
        }
        for (auto swap_iterator = target; swap_iterator < update_iterator; ++swap_iterator) {
            int save = *swap_iterator;
            *swap_iterator = *update_iterator;
            *update_iterator = save;
        }
    }
    return corrected;
}