echo "STARTING PIPELINE"

cd "$(dirname "$0")/.." || exit 1

echo "Project directory: $(pwd)"
echo ""

if [ -d "venv" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
fi

echo ""
echo "Running process_data.py..."
python3 scripts/process_data.py

echo ""
echo "CHECKING OUTPUT FILES"

SUCCESS=true

if [ -f "output/clean_sales.csv" ]; then
    echo "FOUND clean_sales.csv"
else
    echo "MISSING clean_sales.csv"
    SUCCESS=false
fi 

if [ -f "output/sales_by_region.csv" ]; then
    echo "FOUND sales_by_region.csv"
else
    echo "MISSING sales_by_region.csv"
    SUCCESS=false
fi

if [ -f "output/sales_by_product.csv" ]; then
    echo "FOUND sales_by_product.csv"
else
    echo "MISSING sales_by_product.csv"
    SUCCESS=false
fi

if [ -f "output/monthly_revenue.csv" ]; then
    echo "FOUND monthly_revenue.csv"
else
    echo "MISSING monthly_revenue.csv"
    SUCCESS=false
fi

if [ -f "output/salesperson_performance.csv" ]; then
    echo "FOUND salesperson_performance.csv"
else
    echo "MISSING salesperson_performance.csv"
    SUCCESS=false
fi

echo ""

if $SUCCESS; then
    echo "PIPELINE SUCCESSFUL"
else
    echo "PIPELINE INCOMPLETE"
fi