#!/bin/bash
# Sentinel Cardio: DOJ Forensic Sweep with Abhijit Fold (Ethical Gap)

echo "===== INITIATING DOJ SILO AUDIT ====="

DATA_DIR="./data/doj_records"
FOLD_FILE="./data/abhiijit_fold.json"
RESOLVED_FILE="./data/resolved.txt"
REPORT_FILE="audit_report.txt"

# Create empty fold if not exists
if [ ! -f "$FOLD_FILE" ]; then
    echo "[]" > "$FOLD_FILE"
fi

# Clear previous report
> "$REPORT_FILE"

# Scan for sensitive keywords
grep -rnE "REDACTED|OMITTED|CLASSIFIED" "$DATA_DIR" > "$REPORT_FILE"

# Process each line of the report – move sensitive entries to the Fold
while IFS= read -r line; do
    # Extract file path and line number (basic parsing)
    file_path=$(echo "$line" | cut -d: -f1)
    line_num=$(echo "$line" | cut -d: -f2)
    content=$(echo "$line" | cut -d: -f3-)
    
    # Check if this file/line is in a "sensitive context" (e.g., historical / human‑trauma)
    # For now, we treat ANY match as requiring witness. You can later refine.
    if [[ "$file_path" =~ "historical" ]] || [[ "$content" =~ "Grays Harbor" ]] || [[ "$content" =~ "judicial" ]]; then
        # Move to Abhijit fold
        record_id=$(echo "$file_path:$line_num" | sha256sum | cut -c1-16)
        jq --arg id "$record_id" \
           --arg path "$file_path" \
           --arg line "$line_num" \
           --arg content "$content" \
           '. += [{"record_id": $id, "file": $path, "line": $line, "content": $content, "custos": {"reason": "Historical sensitivity – requires witness", "date": "'$(date -u +"%Y-%m-%dT%H:%M:%SZ")'"}}]' \
           "$FOLD_FILE" > "$FOLD_FILE.tmp" && mv "$FOLD_FILE.tmp" "$FOLD_FILE"
    else
        # Normal resolved record
        echo "$line" >> "$RESOLVED_FILE"
    fi
done < "$REPORT_FILE"

# Append PHCA placeholder
echo "===== ANALYZING FOR FIFTH MANIFOLD RESONANCE =====" >> "$REPORT_FILE"
echo "PHCA analysis pending enhancements" >> "$REPORT_FILE"

# Calculate metrics (total records = resolved + fold)
resolved_count=$(wc -l < "$RESOLVED_FILE" 2>/dev/null || echo 0)
fold_count=$(jq '. | length' "$FOLD_FILE")
total_records=$((resolved_count + fold_count))

if [ $total_records -eq 0 ]; then
    completion=100
else
    completion=$(echo "scale=2; ($resolved_count / $total_records) * 100" | bc)
fi

# Write metrics.json
cat > "./data/metrics.json" <<EOF
{
  "total_records": $total_records,
  "resolved_count": $resolved_count,
  "abhiijit_fold_count": $fold_count,
  "completion_percent": $completion,
  "last_audit": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
}
EOF

echo "===== AUDIT COMPLETE ====="
echo "Resolved: $resolved_count | Fold: $fold_count | Completion: $completion%"
cat "$REPORT_FILE"