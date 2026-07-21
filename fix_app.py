#!/usr/bin/env python3
"""Comprehensive fixer for App.jsx syntax errors."""
import re, sys

def fix_file():
    # Fix index.html first
    idx = open('index.html').read()
    idx = idx.replace('/src/main.jsx', '/main.jsx')
    open('index.html','w').write(idx)
    print("OK: index.html script path")

    content = open('App.jsx').read()
    fixes = 0

    def fix(old, new, desc):
        nonlocal content, fixes
        if old in content:
            content = content.replace(old, new, 1)
            fixes += 1
            print(f"  OK: {desc}")
        else:
            print(f"  SKIP (not found): {desc}")

    # 1. Remove duplicate LineChart from lucide-react import
    fix('Clipboard, LineChart, DollarSign',
        'Clipboard, DollarSign',
        "Remove LineChart from lucide")

    # 2. Remove duplicate PieChart from lucide-react import
    fix('BarChart2, PieChart, BadgePercent',
        'BarChart2, BadgePercent',
        "Remove PieChart from lucide")

    # 3. Remove second duplicate UtensilsCrossed, ChefHat, CookingPot
    fix('Archive, UtensilsCrossed, ChefHat, CookingPot, Moon,',
        'Archive, Moon,',
        "Remove duplicate UtensilsCrossed/ChefHat/CookingPot")

    # 4. ALERT_PRIORITY broken object - add properties and close it
    fix('// Alert priority colour maps\nconst ALERT_PRIORITY = {\n\n// ── useBulkSelect — table multi-select with actions ─────────────────────────',
        '''// Alert priority colour maps
const ALERT_PRIORITY = {
  critical: { bg: "#FEF2F2", border: "#FCA5A5", dot: "#EF4444", text: "#991B1B", badge: "#FEE2E2", badgeText: "#991B1B" },
  high:     { bg: "#FFFBEB", border: "#FCD34D", dot: "#F59E0B", text: "#92400E", badge: "#FEF3C7", badgeText: "#B45309" },
  medium:   { bg: "#EFF6FF", border: "#93C5FD", dot: "#3B82F6", text: "#1D4ED8", badge: "#DBEAFE", badgeText: "#1E40AF" },
  low:      { bg: "#F0FDF4", border: "#86EFAC", dot: "#22C55E", text: "#15803D", badge: "#DCFCE7", badgeText: "#166534" },
};

// ── useBulkSelect — table multi-select with actions ─────────────────────────''',
        "ALERT_PRIORITY object")

    # 5. Remove orphaned ALERT_PRIORITY properties
    fix('''}

  critical: { bg: "#FEF2F2", border: "#FCA5A5", dot: "#EF4444", text: "#991B1B", badge: "#FEE2E2", badgeText: "#991B1B" },
  high:     { bg: "#FFFBEB", border: "#FCD34D", dot: "#F59E0B", text: "#92400E", badge: "#FEF3C7", badgeText: "#B45309" },
  medium:   { bg: "#EFF6FF", border: "#93C5FD", dot: "#3B82F6", text: "#1D4ED8", badge: "#DBEAFE", badgeText: "#1E40AF" },
  low:      { bg: "#F0FDF4", border: "#86EFAC", dot: "#22C55E", text: "#15803D", badge: "#DCFCE7", badgeText: "#166534" },
};

// ── Dark mode CSS injected into document head ─────────────────────────────''',
        '''}

// ── Dark mode CSS injected into document head ─────────────────────────────''',
        "Orphaned ALERT_PRIORITY props")

    # 6. Prose: "this is a view"
    fix('}\n\n this is a view, not a table.\n/*',
        '}\n\n// this is a view, not a table.\n/*',
        "Prose: 'this is a view'")

    # 7. Prose: "t's supposed to"
    fix("}\n\nt's supposed to\n// summarize.\nfunction PartiesLedger",
        "}\n\n// t's supposed to summarize.\nfunction PartiesLedger",
        "Prose: 't's supposed to'")

    # 8. Orphaned comment before Contacts
    fix('}\n\n------------------------- */\n\nfunction Contacts() {',
        '}\n\n// -------------------------\n\nfunction Contacts() {',
        "Orphaned comment before Contacts")

    # 9. Prose: "ather than"
    fix('}\n\nather than a separate record.\nfunction SupplierPortal',
        '}\n\n// ather than a separate record.\nfunction SupplierPortal',
        "Prose: 'ather than'")

    # 10. Broken comment: "wou\nld look"
    fix('// with a formula that wou\nld look precise and be wrong.\nfunction FinancialRatiosView',
        '// with a formula that would look precise and be wrong.\nfunction FinancialRatiosView',
        "Broken comment: 'wou\\nld look'")

    # 11. JSX fragment for sibling buttons
    fix('''        {tab !== "subscriptions" && (
          <button
            onClick={() => setShowForm(true)}
            className="btn-primary text-white text-[13px] font-medium px-3.5 py-2 rounded-lg flex items-center justify-center gap-1.5 shadow-sm transition-colors shrink-0"
          >
            <Plus size={15} /> New {tab === "quotations" ? "Quotation" : tab === "orders" ? "Order" : "Invoice"}
          </button>
          <button onClick={() => downloadCSV("sales-" + tab, filtered, [{key:"id",label:"ID"},{key:"customer",label:"Customer"},{key:"date",label:"Date"},{key:"status",label:"Status"}])} className="flex items-center gap-1 text-[12.5px] font-medium text-slate-500 border border-slate-200 px-3 py-2 rounded-lg hover:border-[#16A34A] hover:text-[#16A34A] transition-colors"><Download size={13}/>CSV</button>
        )}''',
        '''        {tab !== "subscriptions" && (
          <>
          <button
            onClick={() => setShowForm(true)}
            className="btn-primary text-white text-[13px] font-medium px-3.5 py-2 rounded-lg flex items-center justify-center gap-1.5 shadow-sm transition-colors shrink-0"
          >
            <Plus size={15} /> New {tab === "quotations" ? "Quotation" : tab === "orders" ? "Order" : "Invoice"}
          </button>
          <button onClick={() => downloadCSV("sales-" + tab, filtered, [{key:"id",label:"ID"},{key:"customer",label:"Customer"},{key:"date",label:"Date"},{key:"status",label:"Status"}])} className="flex items-center gap-1 text-[12.5px] font-medium text-slate-500 border border-slate-200 px-3 py-2 rounded-lg hover:border-[#16A34A] hover:text-[#16A34A] transition-colors"><Download size={13}/>CSV</button>
          </>
        )}''',
        "JSX fragment for sibling buttons")

    # 12. submitPayment corrupted ending
    fix('''    setShowPayLink(false);
    notify("Payment recorded · Ref: " + ref);
  });
    setPayOpen(false);
    setPayAmount("");
  }

  return (''',
        '''    setShowPayLink(false);
    notify("Payment recorded · Ref: " + ref);
  }

  return (''',
        "submitPayment corrupted ending")

    # 13. Duplicate totalBudget/totalActual
    fix('''  }).filter(d => d.actual > 0 || d.budget > 0);

  const totalBudget = budgets.rows.reduce((s,b) => s+b.monthlyLimit, 0);
  const totalActual = expenses.filter(e => e.date >= monthStart).reduce((s,e) => s+e.amount, 0);
  const overBudgetCats = chartData.filter(d => d.over).length;''',
        '''  }).filter(d => d.actual > 0 || d.budget > 0);

  const overBudgetCats = chartData.filter(d => d.over).length;''',
        "Duplicate totalBudget/totalActual")

    # 14. SCAN_DOC_TYPES broken array
    fix('}\n\n"TIN Certificate", "Other"];\n\nfunction DocumentScannerView',
        '}\n\nconst SCAN_DOC_TYPES = ["Receipt", "Invoice", "Tax Document", "Business License", "TIN Certificate", "Other"];\n\nfunction DocumentScannerView',
        "SCAN_DOC_TYPES array")

    # 15. Map callback missing closing before </tbody> (WorkingTimetable)
    fix('''                      </td>
                    </tr>
    
              </tbody>''',
        '''                      </td>
                    </tr>
                  )})}
              </tbody>''',
        "Map callback closing (WorkingTimetable)")

    # 16. Split identifier: addCand\nidate
    fix('onSubmit={addCand\nidate} />',
        'onSubmit={addCandidate} />',
        "Split addCandidate identifier")

    # 17. Broken EmptyState in Attendance
    fix('''              {!loading && rows.length === 0 && <tr><td colSpan={6}><EmptyState icon={CalendarCheck} title="No
          </table>''',
        '''              {!loading && rows.length === 0 && <tr><td colSpan={6}><EmptyState icon={CalendarCheck} title="No records" /></td></tr>}
              </tbody>
            </table>''',
        "Broken EmptyState in Attendance")

    open('App.jsx','w').write(content)
    print(f"\nTotal fixes applied: {fixes}")
    return fixes

if __name__ == '__main__':
    fix_file()
