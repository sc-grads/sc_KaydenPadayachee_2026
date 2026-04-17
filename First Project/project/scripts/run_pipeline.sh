echo "Starting the pipeline"

cd "$(dirname "$0")/.." || exit 1

echo "Project directory: $(pwd)"
echo ""

#So the reason i added this line was because if i forgot to enter the venv environment this will automatically turn it on
if [ -d "venv" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
fi

echo ""
echo "Running process_data.py..."
python3 scripts/process_data.py

echo ""
echo "checking files"

SUCCESS=true

if [ -f "output/clean_sales.csv" ]; then
    echo "Created clean_sales.csv"
else
    echo "missing clean_sales.csv"
    SUCCESS=false
fi 

if [ -f "output/sales_by_region.csv" ]; then
    echo "Created sales_by_region.csv"
else
    echo "missing sales_by_region.csv"
    SUCCESS=false
fi

if [ -f "output/sales_by_product.csv" ]; then
    echo "Created sales_by_product.csv"
else
    echo "missing sales_by_product.csv"
    SUCCESS=false
fi

if [ -f "output/monthly_revenue.csv" ]; then
    echo "Created monthly_revenue.csv"
else
    echo "missing monthly_revenue.csv"
    SUCCESS=false
fi

if [ -f "output/salesperson_performance.csv" ]; then
    echo "Created salesperson_performance.csv"
else
    echo "missing salesperson_performance.csv"
    SUCCESS=false
fi

echo ""

if $SUCCESS; then
    echo "The pipeline was completed successfully"
else
    echo "Something happened, check pipeline or logs to find out more"
fi